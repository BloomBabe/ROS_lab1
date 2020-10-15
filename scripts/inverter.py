#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def inverter(data):
    pub = rospy.Publisher('ni_gnirts', String, queue_size=10)
    rospy.loginfo(f'Arbitrary string: {data.data}')

    msg = String()
    msg.data = data.data[::-1]
    rospy.loginfo(f'Inverted arbitrary string: {msg.data}')
    pub.publish(msg) 

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('string_in', String, inverter)
    rospy.spin()

if __name__ == '__main__':
    listener()
