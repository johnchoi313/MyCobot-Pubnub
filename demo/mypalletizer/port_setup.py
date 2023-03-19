import serial
import serial.tools.list_ports

from pymycobot.mypalletizer import MyPalletizer

def setup():
    mc = MyPalletizer(1, 1000000, debug=True)

    return mc

