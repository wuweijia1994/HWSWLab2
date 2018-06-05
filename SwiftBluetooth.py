import serial

class SwiftRobotArm:

    def __init__(self):
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=115200
            # parity=serial.PARITY_ODD,
            # stopbits=serial.STOPBITS_TWO,
            # bytesize=serial.SEVENBITS
        )
        if(self.ser.isOpen()):
            print("The robot arm is in connection.")
        else:
            print("Could not connect to the robot arm.")

    def resetArm(self):
        # self.attachMotors()
        self.pumpStop()
        self.move(100, 0, 150)
        self.rotateMotor(3, 75)

    def move(self, arm_x, arm_y, arm_z = 150, arm_speed = 2000):
        cmd = '#n G0 X' + str(arm_x) + ' Y' + str(arm_y) +' Z' + str(arm_z) + ' F' + str(arm_speed) + '\n'
        self.ser.write(cmd.encode())
        line = self.ser.readline()
        info = "Move arm "
        self.checkCallback(info, line)
        # return line

    def detachMotors(self):
        cmd = '#n M2019\n'
        self.ser.write(cmd.encode())
        line = self.ser.readline()
        info = "Detach all motors "
        self.checkCallback(info, line)
        # return line

    def attachMotors(self):
        cmd = '#n M17\n'
        self.ser.write(cmd.encode())
        line = self.ser.readline()
        info = "Attach all motors "
        self.checkCallback(info, line)
        return line

    def getEndPosition(self):
        cmd = '#n P2220\n'
        self.ser.write(cmd.encode())
        line = self.ser.readline().decode("utf-8")
        OK, x, y, z = line.split(" ")
        x = x[1:]
        y = y[1:]
        z = z[1:]
        return x, y, z

    def pumpWorking(self):
        cmd = "#n M2231 V1\n"
        self.ser.write(cmd.encode())
        line = self.ser.readline()
        info = "Pumping "
        self.checkCallback(info, line)
        return line

    def pumpStop(self):
        cmd = '#n M2231 V0\n'
        self.ser.write(cmd.encode())
        line = self.ser.readline()
        info = "Stop pumping "
        self.checkCallback(info, line)
        return line

    def rotateMotor(self, motor_num, angle):
        cmd = '#n G2202 N' + str(motor_num) + ' V' + str(angle) + '\n'
        self.ser.write(cmd.encode())
        line = self.ser.readline()
        info = "Rotate motor "
        self.checkCallback(info, line)
        return line

    def checkCallback(self, info, line):
        success = line.decode("utf-8")
        # print(success)
        # print(success)
        # success, others = line.split(" ")
        if not success.startswith("OK"):
            print(info + "fails.")
            quit()
        else:
            print(info + "success.")
            # return others

# configure the serial connections (the parameters differs on the device you are connecting to)
