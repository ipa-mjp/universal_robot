#! /usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray


if __name__ == "__main__":
	rospy.init_node('add_collisions_py')
        rate = rospy.Rate(10) # 10hz

	pub = rospy.Publisher("/arm/joint_group_velocity_controller/command", Float64MultiArray, queue_size = 1000)
	rospy.sleep(1.0)

	pub_data = Float64MultiArray()
        for i in range(0, 10):
                pub_data.data = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0] #[-1.0,-1.0,-1.0,-1.0,-1.0,-1.0]
		pub.publish(pub_data)
                rospy.sleep(0.05)
	for i in range(0, 10):
		pub_data.data = [0.0,0.0,0.0,0.0,0.0,0.0]
		pub.publish(pub_data)
		rospy.sleep(0.05)
	

