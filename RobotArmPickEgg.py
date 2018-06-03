import sys, os
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages/')
from time import sleep
import egg
# import cv2

import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200
    # parity=serial.PARITY_ODD,
    # stopbits=serial.STOPBITS_TWO,
    # bytesize=serial.SEVENBITS
)

ser.isOpen()
# ser.write('#n G0 X100 Y100 Z200 F1000\n')

ser.write('#n G0 X100 Y100 Z100 F1000\n')
time.sleep(8)

image = egg.getImage(1)
image_x, image_y = egg.getEggPosition(image)
arm_x, arm_y = egg.xyMapping(image_x, image_y)

print(arm_x, arm_y)
# ser.write()
cmd = '#n G0 X' + str(arm_x) + ' Y' + str(arm_y) +' Z150 F1000\n'
print(cmd)
print('#n G0 X100 Y100 Z100 F1000\n')
ser.write(cmd)
time.sleep(8)
cmd = '#n G0 X' + str(arm_x) + ' Y' + str(arm_y) +' Z100 F1000\n'
ser.write(cmd)

time.sleep(8)

cmd = '#n M2231 V1\n'
ser.write(cmd)

time.sleep(3)

cmd = '#n M2231 V0\n'
ser.write(cmd)

time.sleep(3)

# cmd = '#n G0 X' + str(arm_x) + ' Y' + str(arm_y) +' Z100 F1000\n'
# ser.write(cmd)

# time.sleep(8)
# while True:
#     image = egg.getImage(1)
#     image_x, image_y = egg.getEggPosition(image)
#     arm_x, arm_y = egg.xyMapping(image_x, image_y)
#
#     print(arm_x, arm_y)
#     # ser.write()
#     cmd = '#n G0 X' + str(arm_x) + ' Y' + str(arm_y) +' Z150 F1000\n'
#     print(cmd)
#     print('#n G0 X100 Y100 Z100 F1000\n')
#     ser.write(cmd)
#     time.sleep(5)

# sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


# from uf.wrapper.swift_api import SwiftAPI
# from uf.utils.log import *
#
# #logger_init(logging.VERBOSE)
# #logger_init(logging.DEBUG)
# logger_init(logging.INFO)
#
# print('setup swift ...')
#
# #swift = SwiftAPI(dev_port = '/dev/ttyACM0')
# #swift = SwiftAPI(filters = {'hwid': 'USB VID:PID=2341:0042'})
# swift = SwiftAPI() # default by filters: {'hwid': 'USB VID:PID=2341:0042'}
#
#
# print('sleep 2 sec ...')
# sleep(2)
#
# swift.set_position(10, 0, 0, speed = 1500, timeout = 20)
#
# while True:
#     sleep(1)
