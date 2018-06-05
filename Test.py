
import sys, os
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
from time import sleep
import egg
# import cv2
import SwiftBluetooth

import time
import serial

import RobotArmDetection

if __name__ == "__main__":
    while 1:
        # pass
        image = egg.getImage(1)
        arm_x, arm_y = RobotArmDetection.getEndEffectorPosition(image)
        print(arm_x, arm_y)
    # arm = SwiftBluetooth.SwiftRobotArm()
    # arm.attachMotors()
    # arm.rotateMotor(3, 90)
    # arm.rotateMotor(3, 0)
