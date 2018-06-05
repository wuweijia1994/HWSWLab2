import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import egg
import SwiftBluetooth
import numpy as np
from sklearn import linear_model

if __name__ == "__main__":
    points_number = int(input("Let's begin the calibration of the camera and robotarm\nEnter the points you want."))
    arm = SwiftBluetooth.SwiftRobotArm()

    camera_x = []
    camera_y = []
    robotarm_x = []
    robotarm_y = []

    for index in range(points_number):
        print("Put the egg in a proper position.")
        while(1):
            move_on = input("When you are done, press d. ")
            if(move_on == "d"):
                print("Egg detection is done.")
                break
        cx, cy = egg.eggPositionByCamera(1)

        print("The position of egg is: ")
        print(cx, cy)
        camera_x.append(cx)
        camera_y.append(cy)

        arm.detachMotors()
        print("Please move the robot arm to the top of the egg")

        while(1):
            move_on = input("When you are done, press d. ")
            if(move_on == "d"):
                print("Robot Arm detection is done.")
                break

        arm_x, arm_y, arm_z = arm.getEndPosition()
        print(arm_x, arm_y)
        robotarm_x.append(int(float(arm_x)))
        robotarm_y.append(int(float(arm_y)))

    # Create linear regression object
    # regr = linear_model.LinearRegression()

    # Train the model using the training sets
    # robotarm_y = [1, 2, 3, 4, 5, 6]
    # camera_x = [2, 4, 6, 8, 10 ,12]
    # print(np.asarray(camera_x).reshape((6, 1)).shape)

    # a = np.asarray(camera_x).reshape((6, 1))
    # b = np.asarray(robotarm_y).reshape((6, 1))
    # print(camera_x)
    # print(robotarm_y)
    c = np.polyfit(camera_x, robotarm_y, 1)
    print(c)

    c = np.polyfit(camera_y, robotarm_x, 1)

    print(c)
    # regr.fit(a, b)
    # print(regr.intercept_)

    # regr.fit([camera_y], [robotarm_x])
