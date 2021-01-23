import sys, os, socketio
from dotenv import load_dotenv

import OpenRGB, Led, IO

from IO.Chat import connect as connectChat
from IO.Eventos import connect as connectEventos

load_dotenv()

IP_OPENRGB = os.getenv('IP_OPENRGB')
PORT_OPENRGB = int(os.getenv('PORT_OPENRGB'))

IP_LED = os.getenv('IP_LED')
PORT_LED = int(os.getenv('PORT_LED'))

IP_EVENTOS = os.getenv("IP_EVENTOS")
PORT_EVENTOS = os.getenv("PORT_EVENTOS")

IP_CHAT = os.getenv("IP_CHAT")
PORT_CHAT = os.getenv("PORT_CHAT")

try:
    connectChat(IP_CHAT,PORT_CHAT)
except Exception as e:
    print("No se pudo conectar a ChatTwitch Server por IO", e)
    sys.exit(-1)

try:
    connectEventos(IP_EVENTOS,PORT_EVENTOS)
except Exception as e:
    print("No se pudo conectar a EventosTwitch Server por IO", e)
    sys.exit(-1)



try:
    OpenRGB.connect(IP_OPENRGB,PORT_OPENRGB)
    print("Conectado a OpenRGB Server")
except OSError:
    print("No se pudo conectar a OpenRGB Server")
    sys.exit(-2)

try:
    Led.connect(IP_LED,PORT_LED)
    print("Conectado a Led Server")
except OSError:
    print("No se pudo conectar a Led Server")
    sys.exit(-3)

