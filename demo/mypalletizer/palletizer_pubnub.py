import time
import sys
import os

import serial
import serial.tools.list_ports

from pymycobot.genre import Angle, Coord

from pymycobot.mypalletizer import MyPalletizer

sys.path.append(os.path.dirname(__file__))

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

def setup():
    print("")

    plist = list(serial.tools.list_ports.comports())
    idx = 1
    for port in plist:
        print("{} : {}".format(idx, port))
        idx += 1

    _in = input("\nPlease input 1 - {} to choice:".format(idx - 1))
    port = str(plist[int(_in) - 1]).split(" - ")[0].strip()
    print(port)
    print("")

    baud = 1000000
    _baud = input("Please input baud(default:1000000):")
    try:
        baud = int(_baud)
    except Exception:
        pass
    print(baud)
    print("")

    DEBUG = False
    f = input("Wether DEBUG mode[Y/n]:")
    if f in ["y", "Y", "yes", "Yes"]:
        DEBUG = True

    # mc = MyCobot(port, debug=True)
    mc = MyPalletizer(1, 1000000, debug=DEBUG)
    return mc



def test(mycobot):
    reset = [153.19, 137.81, -153.54, 156.79, 87.27, 13.62]
    print("\nStart check basic options\n")

    mycobot.set_color(255, 255, 0)
    print("::set_color() ==> color {}\n".format("255 255 0"))
    time.sleep(3)

    angles = [0, 0, 0, 0, 0, 0]
    mycobot.send_angles(angles, 100)
    print("::send_angles() ==> angles {}, speed 100\n".format(angles))
    time.sleep(3)

    print("::get_angles() ==> degrees: {}\n".format(mycobot.get_angles()))
    time.sleep(1)

    mycobot.send_angle(Angle.J1.value, 90, 50)
    print("::send_angle() ==> angle: joint1, degree: 90, speed: 50\n")
    time.sleep(4)

    radians = [1, 1, 1, 1, 1, 1]
    mycobot.send_radians(radians, 100)
    print("::send_radians() ==> set radians {}, speed 100\n".format(radians))
    time.sleep(3)

    print("::get_radians() ==> radians: {}\n".format(mycobot.get_radians()))
    time.sleep(1)

    coords = [160, 160, 160, 0, 0, 0]
    mycobot.send_coords(coords, 70, 0)
    print("::send_coords() ==> send coords {}, speed 70, mode 0\n".format(coords))
    time.sleep(3)

    print("::get_coords() ==> coords {}\n".format(mycobot.get_coords()))
    time.sleep(0.5)

    mycobot.send_coord(Coord.X.value, -40, 70)
    print("::send_coord() ==> send coord id: X, coord value: -40, speed: 70\n")
    time.sleep(2)

    print("::set_free_mode()\n")
    mycobot.send_angles(reset, 100)
    time.sleep(5)
    mycobot.release_all_servos()

    print("=== check end ===\n")


if __name__ == "__main__":
    print(
        """
--------------------------------------------
| This file will test basic option method: |
|     set_led_color()                      |
|     send_angles()                        |
|     get_angles()                         |
|     send_angle()                         |
|     send_radians()                       |
|     get_radians()                        |
|     send_coords()                        |
|     get_coords()                         |
|     send_coord()                         |
--------------------------------------------
          """
    )
    time.sleep(3)

    mypalletizer = setup()
    test(mypalletizer)
