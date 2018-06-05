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
    im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(len(contours) > 0):
        camera_x = []
        camera_y = []
        for index in range (len(contours)):
            cnt= contours[index]
            M = cv2.moments(cnt)
            #print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            camera_x.append(cx)
            camera_y.append(cy)

        return camera_x, camera_y
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

    # return int(y * 0.45893878 + 42.01635299), int(x * 0.50576957 -173)0.58324222, -184.05565132
    return int(y * 0.6952352 - 51.54381175), int(x * 0.58324222 - 188.05565132)

def heightFixed(x, y):
    x_offset = 400
    y_offset = 480

    x_new = x + (x - x_offset) * 7.8 / 38
    y_new = y + (y - y_offset) * 7.8 / 38
    return x_new, y_new
