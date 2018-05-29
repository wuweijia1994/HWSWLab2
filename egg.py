import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a VideoCapture object
cap = cv2.VideoCapture(1)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(8, 8))
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('eggContour.avi',fourcc, 10, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()
    if ret == True:
        GrayImage=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        ret,thresh=cv2.threshold(GrayImage,230,255,cv2.THRESH_BINARY)
        # Display the resulting frame
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
        if(len(contours) > 0):
            cnt = contours[0]
            M = cv2.moments(cnt)
            #print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print( cx,cy )
            thresh=cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB)
            cv2.circle(thresh,(cx,cy), 12, (0,0,255), -1)
            cv2.drawContours(thresh, contours, 0, (255,0,255), 3)
            #cv2.waitKey(3)
            cv2.imshow('eggs',thresh)
            # Write the frame into the file 'output.avi'
            out.write(thresh)
            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # Break the loop
    else:
        break

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()
