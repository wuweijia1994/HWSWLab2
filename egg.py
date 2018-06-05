import cv2
import time

def getEggPosition(image):
    import numpy as np
    from matplotlib import pyplot as plt
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(8, 8))
    GrayImage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    ret,thresh=cv2.threshold(GrayImage,230,255,cv2.THRESH_BINARY)

    # Display the resulting frame
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    if(len(contours) > 0):
        cnt = contours[0]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        return cx, cy
    else:
        print("Not Found!")
        return None, None


def getImage(camera):
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        if ret == True:
            break
    cap.release()
    return frame

def eggPositionByCamera(camera):
    while(1):
        frame = getImage(camera)
        x, y = getEggPosition(frame)
        if(x == None):
            print("Did not detect any egg. Please try again")
        else:
            return x, y
        time.sleep(2)

def xyMapping(x, y):

    return int(y * 0.45893878 + 42.01635299), int(x * 0.50576957 -173)
