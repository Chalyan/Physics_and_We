import time

import serial
import struct
from time import sleep
import numpy as np
import random


class Backend:
    def __init__(self, port: str, baudrate: int, wrapper: object):
        self.port = port
        self.baudrate = baudrate
        # self.ser = serial.Serial('COM3', baudrate=self.baudrate, timeout=1)
        self.byte_length = 6000
        self.start_command = b'\xa0\xb0'
        self.stop_command = b'\xa1\xb1'
        self.start_bytes = b'\xff\xa0'
        self.wrapper = wrapper

    @staticmethod
    def random_generator():
         return np.array([(i, random.randint(1, 480)) for i in range(1, 500)])

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
        return_value = 0
        error_instances = 0
        while return_value == 2:
            return_value = self.ser.write(self.start_command)
            sleep(0.01)
            error_instances += 1
            if error_instances > 10:
                raise TimeoutError("Device not responding")

    def stop_device(self):
        return_value = 0
        error_instances = 0
        while return_value == 2:
            return_value = self.ser.write(self.stop_command)
            sleep(0.01)
            error_instances += 1
            if error_instances > 10:
                raise TimeoutError("Device not responding")
