import socketio
import OpenRGB, Led

sio = socketio.Client()

def connect(IP,PORT):
    sio.connect("http://localhost:5000")
    print('Sucessfully connected to WS Server')

@sio.on("handshake")
def handshake(data):
    sio.emit("handshake","leds")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('message')
def message(data):

    color = data["color"]
    username = data["user"]

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
        msg = "El color que elegiste no existe. Colores disponibles: rojo, azul, verde, amarillo, violeta, rosa, naranja y celeste"

    sio.emit('response', msg)
