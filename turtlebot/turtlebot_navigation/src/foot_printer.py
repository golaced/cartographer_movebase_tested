#!/usr/bin/env python

import rospy
import time
import tf
import math
from geometry_msgs.msg import *
from nav_msgs.msg import *


if __name__ == '__main__':

		int xAnt=0.0
        int yAnt=0.0
        int cont=0

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

	        '''
	        #pose.pose.orientation.x = float(data.pose.pose.orientation.x)
	        #pose.pose.orientation.y = float(data.pose.pose.orientation.y)
	        #pose.pose.orientation.z = float(data.pose.pose.orientation.z)
	        #pose.pose.orientation.w = float(data.pose.pose.orientation.w)
	        '''

	        if (xAnt != pose.pose.position.x and yAnt != pose.pose.position.y):
	                pose.header.seq = path.header.seq + 1
	                path.header.frame_id="odom"
	                path.header.stamp=rospy.Time.now()
	                pose.header.stamp = path.header.stamp
	                path.poses.append(pose)

	        #cont=cont+1
	        #rospy.loginfo("Valor del contador: %i" % cont)
	        #if cont>max_append:
		    #	path.poses.pop(0)

	        pub.publish(path)
	        xAnt=pose.pose.orientation.x
	        yAnt=pose.pose.position.y
       		rate.sleep()
