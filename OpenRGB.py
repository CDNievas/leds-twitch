from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from enum import Enum

client = None

def connect(ip, port):
    global client
    client = OpenRGBClient(ip, port, '')
    client.disconnect()

def changeKeyboardColor(color):
    client.connect()
    keyboard = client.get_devices_by_type(DeviceType.KEYBOARD)[0]
    keyboard.set_mode("static")
    keyboard.set_color(color.value)
    client.disconnect()

class Color(Enum):
    RED = RGBColor(255,0,0)
    GREEN = RGBColor(0,255,0)
    BLUE = RGBColor(0,0,255)
    YELLOW = RGBColor(255,255,0)
    SKYBLUE = RGBColor(0,200,255)
    VIOLET = RGBColor(100,0,255)
    PINK = RGBColor(255,0,255)
    ORANGE = RGBColor(255,185,0)