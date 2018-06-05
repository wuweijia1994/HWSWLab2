
import sys, os
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
from time import sleep
import egg
# import cv2
import SwiftBluetooth

import time
import serial

if __name__ == "__main__":
    arm = SwiftBluetooth.SwiftRobotArm()
    arm.attachMotors()
    arm.rotateMotor(3, 90)
    # arm.rotateMotor(3, 0)
