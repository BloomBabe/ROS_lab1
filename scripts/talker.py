#!/usr/bin/env python
# license removed for brevity
import rospy
import random
import string
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('string_in', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        letters = string.ascii_lowercase
        msg = String()
        msg.data = ''.join(random.choice(letters) for i in range(10))
        rospy.loginfo(f'sended data: {msg.data}')
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
