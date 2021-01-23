import socketio
import OpenRGB, Led

EventosIO = socketio.Client()

from IO.Chat import sio as ChatIO

def connect(ip,port):
    EventosIO.connect("http://{}:{}".format(ip,port))
    print('Conectado a EventosTwitch Server por IO')

@EventosIO.on("handshake")
def handshake(data):
    EventosIO.emit("handshake","leds")

@EventosIO.event
def disconnect():
    print("Desconectado de EventosTwitch")

@EventosIO.on('command')
def message(data):

    idRedemption = data["idRedemption"]
    color = data["color"]
    username = data["user"]
    idReward = data["idReward"]

    statusOk = True
    msg = "Color cambiado a {} por @{}".format(color,username)

    if color == "rojo":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.RED)
        Led.changeLedsColor(Led.Color.RED)
    elif color == "verde":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.GREEN)
        Led.changeLedsColor(Led.Color.GREEN)
    elif color == "azul":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.BLUE)
        Led.changeLedsColor(Led.Color.BLUE)
    elif color == "amarillo":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.YELLOW)
        Led.changeLedsColor(Led.Color.YELLOW)
    elif color == "celeste":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.SKYBLUE)
        Led.changeLedsColor(Led.Color.SKYBLUE)
    elif color == "violeta":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.VIOLET)
        Led.changeLedsColor(Led.Color.VIOLET)
    elif color == "rosa":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.PINK)
        Led.changeLedsColor(Led.Color.PINK)
    elif color == "naranja":
        OpenRGB.changeKeyboardColor(OpenRGB.Color.ORANGE)
        Led.changeLedsColor(Led.Color.ORANGE)
    else:
        msg = "@{}, el color que elegiste no existe. Se te han devuelto los puntos".format(username)
        statusOk = False
 
    ChatIO.emit('response', msg)

    if(statusOk):
        EventosIO.emit("success",{"idRedemption":idRedemption, "idReward":idReward})
    else:
        EventosIO.emit("error",{"idRedemption":idRedemption, "idReward":idReward})
