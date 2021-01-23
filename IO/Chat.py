
import socketio

sio = socketio.Client()

def connect(ip,port):
    sio.connect("http://{}:{}".format(ip,port))
    print('Conectado a ChatTwitch Server por IO')

@sio.on("handshake")
def handshake(data):
    sio.emit("handshake","leds")

@sio.event
def disconnect():
    print("Desconectado de ChatTwitch")