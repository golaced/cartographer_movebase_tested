#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include <nav_msgs/Path.h>
#include <geometry_msgs/PoseStamped.h>
#include <vector>

using std::vector;

int main(int argc, char** argv)
{
	ros::init(argc,argv,"foot_printer");
	ros::NodeHandle n;
	ros::Publisher pub=n.advertise<nav_msgs::Path>("/path",10);
	tf::TransformListener listener;
	ros::Rate rate(100);
	float xAnt=0.0;
	float yAnt=0.0;
	nav_msgs::Path path;
        
	vector<geometry_msgs::PoseStamped> poses;
	
	while(n.ok())
		{
			tf::StampedTransform transform;

			try{
				listener.waitForTransform("map","base_link",ros::Time(0),ros::Duration(3.0));
				listener.lookupTransform("map","base_link",ros::Time(0),transform);
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

			if (xAnt+0.01<pose.pose.position.x or pose.pose.position.x<xAnt-0.01 or yAnt+0.01<pose.pose.position.y or pose.pose.position.y<yAnt-0.01){
					pose.header.seq=path.header.seq+1;
					path.header.frame_id="/map";
					path.header.stamp=ros::Time::now();
					pose.header.stamp=path.header.stamp;
					poses.push_back(pose);
					path.poses= poses;
					pub.publish(path);
				}

			xAnt=pose.pose.position.x;
			yAnt=pose.pose.position.y;
			//rate.sleep();
		}

}

