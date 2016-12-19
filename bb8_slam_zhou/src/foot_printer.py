#!/usr/bin/env python

import rospy
import time
import tf
import math
from geometry_msgs.msg import *
from nav_msgs.msg import *


if __name__ == '__main__':

	xAnt=0.0
        yAnt=0.0

        rospy.init_node('foot_printer')

        pub=rospy.Publisher('/path',Path, queue_size=1)

        path=Path()

        listener=tf.TransformListener()

       	rate=rospy.Rate(10)

       	listener.waitForTransform("/map", "/base_link", rospy.Time(0),  rospy.Duration(4.0))

       	while not rospy.is_shutdown():
       		try:
       			(trans,rot)=listener.lookupTransform('/map','/base_link',rospy.Time(0))
       		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
       			continue
       		#print ('x= %s, y= %s, z=%s' % (trans[0],trans[1],trans[2]))

	        pose = PoseStamped()
	        pose.header.frame_id = "/map"
	        pose.pose.position.x = trans[0]
	        pose.pose.position.y = trans[1]
                #print pose

	        if (xAnt != pose.pose.position.x or yAnt != pose.pose.position.y):
	                pose.header.seq = path.header.seq + 1
	                path.header.frame_id="/map"
	                path.header.stamp=rospy.Time.now()
	                pose.header.stamp = path.header.stamp
	                path.poses.append(pose)
	                pub.publish(path)
	        xAnt=pose.pose.position.x
	        yAnt=pose.pose.position.y
       		rate.sleep()
