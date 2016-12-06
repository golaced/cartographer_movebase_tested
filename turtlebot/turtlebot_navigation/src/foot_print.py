#!/usr/bin/env python

import rospy
import sys
import time
from geometry_msgs.msg import *
from nav_msgs.msg import *



def callback(data):
        global xAnt
        global yAnt
        global cont
        pose = PoseStamped()
        pose.header.frame_id = "odom"
        pose.pose.position.x = float(data.pose.pose.position.x)
        pose.pose.position.y = float(data.pose.pose.position.y)
        pose.pose.orientation.x = float(data.pose.pose.orientation.x)
        pose.pose.orientation.y = float(data.pose.pose.orientation.y)
        pose.pose.orientation.z = float(data.pose.pose.orientation.z)
        pose.pose.orientation.w = float(data.pose.pose.orientation.w)

        if (xAnt != pose.pose.position.x and yAnt != pose.pose.position.y):
                pose.header.seq = path.header.seq + 1
                path.header.frame_id="odom"
                path.header.stamp=rospy.Time.now()
                pose.header.stamp = path.header.stamp
                path.poses.append(pose)

        cont=cont+1

        rospy.loginfo("Valor del contador: %i" % cont)
        if cont>max_append:
        	path.poses.pop(0)

        pub.publish(path)
        xAnt=pose.pose.orientation.x
        yAnt=pose.pose.position.y
        return path


if __name__ == '__main__':
        #Variable initialization
        global xAnt
        global yAnt
        global cont
        xAnt=0.0
        yAnt=0.0
        cont=0
        rospy.init_node('foot_printer')
        if not rospy.has_param("~max_list_append"):
                rospy.logwarn('The parameter max_list_append dont exists')
        max_append = rospy.set_param("~max_list_append",100)
        max_append = 100000
        if not (max_append > 0):
                rospy.logwarn('The parameter max_list_append not is correct')
                sys.exit()
        pub = rospy.Publisher('/path', Path, queue_size=1)
        path = Path()
        msg = Odometry()
        msg = rospy.Subscriber('/odom', Odometry, callback)
        rate = rospy.Rate(10) # 30hz

    	try:
                while not rospy.is_shutdown():
                    rate.sleep()
        except rospy.ROSInterruptException:
                pass
