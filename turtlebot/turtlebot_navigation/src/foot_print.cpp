#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include <nav_msgs/Path.h>
#include <geometry_msgs/PoseStamped.h>


int main(int argc, char** argv)
{
	ros::init(argc,argv,"foot_printer");
	ros::NodeHandle n;
	ros::Publisher pub=n.advertise<nav_msgs::Path>("/path",10);
	tf::TransformListner listener;
	ros::Rate rate(10);
	float xAnt=0.0;
	float yAnt=0.0;
	nav_msgs::Path path;

	while(n.ok())
		{
			tf::StampedTransform transform;

			try{
				listener.lookupTransform("/map","/base_link",ros::Time(0),transform);
			}

			catch (tf::TransformException ex)
			{
				ROS_ERROR("%s",ex.what());
				ros::Duration(1.0).sleep();
			}

			geometry_msgs::PoseStamped pose;
			pose.header.frame_id="/map";
			pose.pose.position.x=transform.getOrigin().x();
			pose.pose.position.y=transform.getOrigin().y();

			if (xAnt!=pose.pose.position.x or yAnt!=pose.pose.position.y){
					pose.header.seq=path.header.seq+1;
					path.header.frame_id="/map";
					path.header.stamp=rospy::Time::now();
					pose.header.stamp=path.header.stamp;
					pub.publish(path);
				}

			xAnt=pose.pose.position.x;
			yAnt=pose.pose.position.y;
			rate.sleep();
		}

}



