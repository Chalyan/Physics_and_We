import serial

class Backend:
    def __init__(self, port: str, baudrate: int, stopbit: int):
        self.port = port
        self.baudrate = baudrate
        self.ser = None