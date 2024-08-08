import serial
import struct


class Backend:
    def __init__(self, port: str, baudrate: int):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial('COM3', baudrate=self.baudrate, timeout=1)
        self.byte_length = 6000
        self.start_command = b''
        self.stop_command = b''
        self.start_bytes = b''

    def read_data(self, number_of_instances):

        buffer = bytearray()
        data_in_uint16 = []
        reading = True

        while reading:
            raw_data = self.ser.read(self.byte_length * (number_of_instances + 1))
            if raw_data:
                buffer.extend(raw_data)

                while len(buffer) >= self.byte_length:
                    index = buffer.find(self.start_bytes)

                    if index == -1:
                        reading = False
                    elif index > 0:
                        buffer = buffer[index:]

                    if len(buffer) >= self.byte_length:
                        payload = buffer[len(self.start_bytes):self.byte_length]
                        buffer = buffer[self.byte_length:]

                        if len(payload) % 2 != 0:
                            payload = payload[:-1]

                        data = struct.unpack('<2H', payload)

                        data_in_uint16.extend(data)
                    else:
                        reading = False
        return data_in_uint16

    def start_device(self):
        self.ser.write(self.start_command)

    def stop_device(self):
        self.ser.write(self.stop_command)

