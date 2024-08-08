import serial
import struct
from time import sleep
import numpy as np


class Backend:
    def __init__(self, port: str, baudrate: int, wrapper: object):
        self.port = port
        self.baudrate = baudrate
        # self.ser = serial.Serial('COM3', baudrate=self.baudrate, timeout=1)
        self.byte_length = 6000
        self.start_command = b'0xa0b0'
        self.stop_command = b'0xa1b1'
        self.start_bytes = b'0xffa0'
        self.wrapper = wrapper

    def read_data1(self, number_of_instances):
        print(number_of_instances)
        custom_data = np.array([
            [1, 10],
            [2, 20],
            [3, 15],
            [4, 25],
            [5, 30],
            [6, 18],
            [7, 22],
            [8, 28],
            [9, 24],
            [10, 30]
        ])
        return custom_data

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
        return_value = b'0x00'
        error_instances = 0
        while return_value == b'0x00':
            return_value = self.ser.write(self.start_command)
            sleep(0.01)
            error_instances += 1
            if error_instances > 10:
                break

    def stop_device(self):
        return_value = b'0x00'
        error_instances = 0
        while return_value == b'0x00':
            return_value = self.ser.write(self.stop_command)
            sleep(0.01)
            error_instances += 1
            if error_instances > 10:
                break
