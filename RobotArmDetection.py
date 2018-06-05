# import the necessary packages
import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse

import cv2
import imutils
import time


import cv2
import numpy as np
from matplotlib import pyplot as plt

def getEndEffectorPosition(frame):
    greenLower = (135, 55, 66)
    greenUpper = (255, 255, 255)
    pts = deque(maxlen=64)

    if frame is None:
        print("frame is none.")
        quit()

    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    	# find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        # only proceed if the radius meets a minimum size
        if radius > 10:
            return int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
        else:
            print("Did not found arm!")
            return None, None
    else:
        print("Did not found arm!")
        return None, None
    		# draw the circle and centroid on the frame,
    		# then update the list of tracked points
    		# cv2.circle(frame, (int(x), int(y)), int(radius),
    			# (0, 255, 255), 2)
    		# cv2.circle(frame, center, 5, (0, 0, 255), -1)


def getImage(camera = 1):
    cap = cv2.VideoCapture(camera)
    while True:
        ret, frame = cap.read()
        if ret == True:
            break
    cap.release()
    return frame

def armPositionByCamera(camera = 1):
    while(1):
        frame = getImage(camera)
        x, y = getEndEffectorPosition(frame)
        if(x == None):
            print("Did not detect the arm. Please try again")
        else:
            return x, y
        time.sleep(2)
# # update the points queue
# pts.appendleft(center)
# 	# loop over the set of tracked points
# for i in range(1, len(pts)):
# 	# if either of the tracked points are None, ignore
# 	# them
# 	if pts[i - 1] is None or pts[i] is None:
# 		continue
#
# 	# otherwise, compute the thickness of the line and
# 	# draw the connecting lines
# 	thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
# 	cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
#
# # show the frame to our screen
# cv2.imshow("Frame", frame)
# key = cv2.waitKey(1) & 0xFF
#
# # if the 'q' key is pressed, stop the loop
# if key == ord("q"):
# 	break
#
# # if we are not using a video file, stop the camera video stream
# if not args.get("video", False):
# 	vs.stop()
#
# # otherwise, release the camera
# else:
# 	vs.release()
#
# # close all windows
# cv2.destroyAllWindows()
