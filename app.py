import sys, os, socketio
from dotenv import load_dotenv

import OpenRGB, Led, WS

load_dotenv()

IP_OPENRGB = os.getenv('IP_OPENRGB')
PORT_OPENRGB = int(os.getenv('PORT_OPENRGB'))

IP_LED = os.getenv('IP_LED')
PORT_LED = int(os.getenv('PORT_LED'))

IP_WS = os.getenv("IP_WS")
PORT_WS = os.getenv("PORT_WS")

try:
    WS.connect(IP_WS,PORT_WS)
except Exception as e:
    print("Can't connect to WS Server.", e)
    sys.exit(-1)

try:
    OpenRGB.connect(IP_OPENRGB,PORT_OPENRGB)
    print("Sucessfully connected to OpenRGB Server")
except OSError:
    print("Can't connect to OpenRGB Server at {}:{}".format(IP_OPENRGB,PORT_OPENRGB))
    sys.exit(-2)

try:
    Led.connect(IP_LED,PORT_LED)
    print("Sucessfully connected to Led Server")
except OSError:
    print("Can't connect to Led Server at {}:{}".format(IP_LED,PORT_LED))
    sys.exit(-3)



