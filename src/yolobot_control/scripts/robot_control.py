#!/usr/bin/python3
import os, sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import Header, String, Int32
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Joy

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import cv2
bridge = CvBridge()

import threading
import time
global vel_msg

# global vel_msg_lock1,vel_msg_lock2, vel_msg_lock3


vel_msg = Twist()

# vel_msg_lock = threading.Lock()

class Commander(Node):

    def __init__(self):
        super().__init__('commander')
        self.publisher_ = self.create_publisher(Twist, '/yolobot/cmd_vel', 10)
        # print("commander node started")
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.vel_msg_lock1 = False
        self.vel_msg_lock2 = False
        self.vel_msg_lock3 = False
        self.vel_msg_lock4 = False
        self.vel_msg_lock5 = False
        self.vel_msg_lock6 = False
        self.vel_msg_lock7 = False
        self.vel_msg_lock8 = False
        self.vel_msg_lock9 = False
        self.vel_msg_lock10 = False
        self.vel_msg_lock11 = False
        self.vel_msg_lock12 = False
        self.vel_msg_lock13 = False
        self.vel_msg_lock14 = False
        self.vel_msg_lock15 = False
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.count5 = 0
        self.count6 = 0
        self.count7 = 0

    def timer_callback(self):
        # global vel_msg ,vel_msg_lock
        # print("timer_callback")
        
        # print("---Vel_msg---:",vel_msg)
        # vel_msg.linear.x = 0.1
        # vel_msg.linear.y = 0.0
        # vel_msg.angular.z = -0.5

        # Sequence of twist commands to follow a specific path
        # vel_msg.linear.x = 0.1  # Move straight for some time
        # vel_msg.linear.y = 0.0
        # vel_msg.angular.z = 0.0
        # self.publisher_.publish(vel_msg)
        # rclpy.spin_once(commander)
        # time.sleep(3)  # Sleep for 5 seconds

        #go straight
        if not self.vel_msg_lock1:

            while self.count1 < 3:
                vel_msg.linear.x = 0.10 
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = 0.00
                self.publisher_.publish(vel_msg)
                time.sleep(10)
                self.count1 += 1
            self.vel_msg_lock1 = True
          
    
        #go right
        if not self.vel_msg_lock2 and self.vel_msg_lock1:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = -0.4 
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock2 = True


        #go straight
        if not self.vel_msg_lock3 and self.vel_msg_lock2:

            while self.count2 < 5:
                vel_msg.linear.x = 0.1 
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = -0.02
                self.publisher_.publish(vel_msg)
                time.sleep(10)
                self.count2 += 1
            self.vel_msg_lock3 = True
            
        #go right
        if not self.vel_msg_lock4 and self.vel_msg_lock3:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = -0.4 
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock4 = True

        #go straight
        if not self.vel_msg_lock5 and self.vel_msg_lock4:

            while self.count3 < 3:
                vel_msg.linear.x = 0.15 
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = -0.01
                self.publisher_.publish(vel_msg)
                time.sleep(10)
                self.count3 += 1
            self.vel_msg_lock5 = True

        #go right
        if not self.vel_msg_lock6 and self.vel_msg_lock5:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = -0.4 
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock6 = True

        #go straight
        if not self.vel_msg_lock7 and self.vel_msg_lock6:

            while self.count4 < 2:
                vel_msg.linear.x = 0.1
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = -0.01
                self.publisher_.publish(vel_msg)
                time.sleep(10)
                self.count4 += 1
            self.vel_msg_lock7 = True

        #go right
        if not self.vel_msg_lock8 and self.vel_msg_lock7:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = -0.4 
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock8 = True
        
        #go straight
        if not self.vel_msg_lock9 and self.vel_msg_lock8:

            while self.count5 < 5:
                vel_msg.linear.x = 0.1
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = -0.01
                self.publisher_.publish(vel_msg)
                time.sleep(10)
                self.count5 += 1
            self.vel_msg_lock9 = True 
        
        #go left
        if not self.vel_msg_lock10 and self.vel_msg_lock9:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = 0.4 
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock10 = True
      
        #go straight
        if not self.vel_msg_lock11 and self.vel_msg_lock10:

            while self.count6 < 3:
                vel_msg.linear.x = 0.1
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = -0.01
                self.publisher_.publish(vel_msg)
                time.sleep(8)
                self.count6 += 1
            self.vel_msg_lock11 = True 
            
        #go left
        if not self.vel_msg_lock12 and self.vel_msg_lock11:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = 0.4 
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock12 = True
        
        #go straight
        if not self.vel_msg_lock13 and self.vel_msg_lock12:

            while self.count7 < 2:
                vel_msg.linear.x = 0.1
                vel_msg.linear.y = 0.0
                vel_msg.angular.z = -0.01
                self.publisher_.publish(vel_msg)
                time.sleep(10)
                self.count7 += 1
            self.vel_msg_lock13 = True
            
        if not self.vel_msg_lock14 and self.vel_msg_lock13:

            vel_msg.linear.x = 0.0 
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = 0.8
            self.publisher_.publish(vel_msg)
            time.sleep(1.7)
            self.vel_msg_lock14 = True
            
        if not self.vel_msg_lock15 and self.vel_msg_lock14:

            vel_msg.linear.x = 0.0
            vel_msg.linear.y = 0.0
            vel_msg.angular.z = 0.00
            self.publisher_.publish(vel_msg)
            self.vel_msg_lock15 = True
        # vel_msg.linear.x = 0.1 
        # vel_msg.linear.y = 0.0
        # vel_msg.angular.z = 0.0 # Stop the robot
        # self.publisher_.publish(vel_msg)
        # time.sleep(4)

        # vel_msg.angular.z = -0.5  # Turn right for some time
        # # self.publisher_.publish(vel_msg)
        # rclpy.spin_once(commander)
        # rclpy.sleep(3)  # Sleep for 3 seconds

        # vel_msg.angular.z = 0.0  # Stop the robot
        # # self.publisher_.publish(vel_msg)
        # rclpy.spin_once(commander)
        # rclpy.sleep(1)  # Stop for 1 second

        # vel_msg.linear.x = 0.1  # Move straight again for some time
        # # self.publisher_.publish(vel_msg)
        # rclpy.spin_once(commander)
        # rclpy.sleep(5)  # Sleep for 5 seconds

        # vel_msg.linear.x = 0.0  # Stop at the end
        # # self.publisher_.publish(vel_msg)
        # rclpy.spin_once(commander)

        
        
        # self.publisher_.publish(vel_msg)
        # self.publisher_.publish(vel_msg)

class Joy_subscriber(Node):

    def __init__(self):
        # print("Initializing Joy_subscriber node...")
        super().__init__('joy_subscriber')
        print("joy_subscriber node started")

        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, data):
        print("listener_callback")
        # vel_msg.linear.x = data.axes[1]
        # vel_msg.linear.y = 0.0
        # vel_msg.angular.z = data.axes[0] 
    
        # vel_msg.linear.x = 50.0
        # vel_msg.linear.y = 0.0
        # vel_msg.angular.z = -30.0
        # print("---Vel_msg Updated---:", vel_msg)
       

if __name__ == '__main__':


    # print("main")
    rclpy.init(args=None)
    
    commander = Commander()
    joy_subscriber = Joy_subscriber()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(commander)
    executor.add_node(joy_subscriber)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()
    rate = commander.create_rate(2)
    try:
        while rclpy.ok():
            # print("main while")
            rate.sleep()
    except KeyboardInterrupt:
        pass
    
    rclpy.shutdown()
    executor_thread.join()

