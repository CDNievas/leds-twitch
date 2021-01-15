import socket
from enum import Enum

client = None

def connect(ip, port):
    global client
    client = LedClient(ip, port)

def changeLedsColor(color):
    global client
    client.connect()
    client.changeLedsColor(color)
    client.disconnect()

class LedClient:

    ip = None
    port = None
    s = None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip,port))
        self.s.close()

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))

    def changeLedsColor(self,color):
        self.s.send(color.value)

    def disconnect(self):
        self.s.close()

class Color(Enum):
    RED = b"\x31\xFF\x00\x00\x00\x00\x0F\x3F"
    GREEN = b"\x31\x00\xFF\x00\x00\x00\x0F\x3F"
    BLUE = b"\x31\x00\x00\xFF\x00\x00\x0F\x3F"
    YELLOW = b"\x31\xFF\xFF\x00\x00\x00\x0F\x3E"
    SKYBLUE = b"\x31\x00\xFF\xFF\x00\x00\x0F\x3E"
    VIOLET = b"\x31\x82\x00\xFF\x00\x00\x0F\xC1"
    PINK = b"\x31\xFF\x00\xFF\x00\x00\x0F\x3E" 
    ORANGE = b"\x31\xFF\x6D\x00\x00\x00\x0F\xAC"