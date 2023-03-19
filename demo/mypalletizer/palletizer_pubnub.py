import time
import sys
import os

import serial
import serial.tools.list_ports

from pymycobot.genre import Angle, Coord
from pymycobot.mypalletizer import MyPalletizer

from ColorPrinter import *

sys.path.append(os.path.dirname(__file__))

#Angle Example: https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.3_angle.html
#Coord Example: https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.3_coord.html
#Gripper Example: https://docs.elephantrobotics.com/docs/gitbook-en/7-ApplicationBasePython/7.5_gripper.html

'''
json schema{
    “mouse_x”: float (-100 ~100)
    “mouse_y”: float (-100 ~100)
    “left_click_down”: boolean
    “left_click_up”: boolean
    “right_click_down”: boolean
    “right_click_up”: boolean
    “mouse_wheel”: float (translate into -100 ~ 100, like a scroll bar position)
    “space_key_down”: boolean
    “space_key_up”: boolean
}
'''

#Find and connect port
def getPorts(portIndex = 0):
    #print all ports
    plist = list(serial.tools.list_ports.comports())
    idx = 1
    for port in plist:
        print("{} : {}".format(idx, port))
        idx += 1
    #get the specified port and return it
    portName = str(plist[portIndex]).split(" - ")[0].strip()
    return portName

#ANGLES TEST
def angle_test(mp):
    printRed("Testing Angles...")
    mp.set_color(255,0,0)

    mp.send_angles([0, 0, 0, 0,], 50)
    time.sleep(2)

    mp.send_angle(1,20,50) # Move joint 1 to the 50 position
    time.sleep(2)

    for num in range(2):
        mp.send_angle(2,20,50)
        time.sleep(2)
        mp.send_angle(2,(-20),50)
        time.sleep(2)
    
    mp.send_angles([-0.87, 41.66, -12.13, -0.17], 50) # make robot arms reach the specified position
    mp.release_all_servos() # Let the robotic arm relax, you can manually swing the robotic arm

    coords = [160, 160, 160, 0, 0, 0]
    mp.send_coords(coords, 70, 0)
    mp.send_coord(Coord.X.value, -40, 70)

#COORD TEST
def coord_test(mp):
    printGreen("Testing Coords...")
    mp.set_color(0,255,0)

    coords = mp.get_coords() # # Get the current coordinates and pose of the head
    print(coords)

    mp.send_coords([187.8, 42.1, 183.3, -159.6], 80, 0) #Plan the route at random, let the head reach the coordinates of [57.0, -107.4, 316.3] in an non-linear manner at the speed is 80mm/s
    time.sleep(2)
    mp.send_coords([207.9, 47, 49.3,-159.69], 80, 0) # Plan the route at random, let the head reach the coordinates of [207.9, 47, 49.3,-159.69] in an non-linear manner at the speed is 80mm/s
    time.sleep(2)

    #To change only the x-coordinate of the head, set the x-coordinate of the head to 20. Let it plan the route at random and move the head to the changed position at a speed of 70mm/s
    mp.send_coord(Coord.X.value, 20, 50)

#GRIPPER TEST
def gripper_test(mp):
    printBlue("Testing Gripper...")
    mp.set_color(0,0,255)

    mp.send_angle(2, 30, 50) # let joint2 move to 30 degree at the speed of 50
    time.sleep(2)

    #set a variable num, and then set a loop
    for num in range(2):
        mp.set_gripper_state(0,70) #let gripper open at the speed of 70
        time.sleep(2)
        mp.set_gripper_state(1, 70) # let gripper close at the speed of 70
        time.sleep(2)


#run the program
if __name__ == "__main__":
    mypalletizer = MyPalletizer(getPorts(0), 1000000, debug=True)

    gripper_test(mypalletizer)
    time.sleep(2)

    angle_test(mypalletizer)
    time.sleep(2)

    coord_test(mypalletizer)
    time.sleep(2)

