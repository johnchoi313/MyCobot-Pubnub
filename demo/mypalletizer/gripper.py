import os
import time
import sys

import serial
import serial.tools.list_ports

from pymycobot.mycobot import MyCobot
from pymycobot.mypalletizer import MyPalletizer
from pymycobot.genre import Angle, Coord

sys.path.append(os.path.dirname(__file__))

def gripper_test(mc):
    print("Start check IO part of api\n")
    # print()

    flag = mc.is_gripper_moving()
    print("Is gripper moving: {}".format(flag))
    time.sleep(1)

    # Set the current position to (2048).
    # Use it when you are sure you need it.
    # Gripper has been initialized for a long time. Generally, there
    # is no need to change the method.
    # mc.set_gripper_ini()

    mc.set_encoder(7, 2048)
    time.sleep(3)
    mc.set_encoder(7, 1300)
    time.sleep(3)

    # set_gripper_value has some bug, just can close.
    mc.set_gripper_value(2048, 70)
    time.sleep(5)
    mc.set_gripper_value(1500, 70)
    time.sleep(5)

    mc.set_gripper_state(0, 70)
    time.sleep(5)
    mc.set_gripper_state(1, 70)
    time.sleep(5)

    print("")
    print(mc.get_gripper_value())


if __name__ == "__main__":

    plist = list(serial.tools.list_ports.comports())
    idx = 1
    for port in plist:
        print("{} : {}".format(idx, port))
        idx += 1

    portIndex = 0
    port = str(portIndex).split(" - ")[0].strip()
    

    mycobot = MyPalletizer(port, 1000000, debug=True)
    gripper_test(mycobot)


