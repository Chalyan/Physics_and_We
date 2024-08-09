import serial
import struct
from time import sleep
import numpy as np


class Backend:
    def __init__(self, port: str, baudrate: int, wrapper: object):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial('COM7', baudrate=self.baudrate, timeout=1)
        self.byte_length = 7390
        self.start_command = b'\xa0\xb0'
        self.stop_command = b'\xa1\xb1'
        self.start_bytes = b'\xa0\xff'
        self.wrapper = wrapper

    def read_from_device(self, number_of_instances):
        buffer = bytearray()
        data_in_uint16 = []
        raw_data = self.ser.read(self.byte_length * (number_of_instances + 1))
        if raw_data:

            buffer.extend(raw_data)
            while len(buffer) >= self.byte_length:
                index = buffer.find(self.start_bytes)

                if index == -1:
                    break
                elif index > 0:
                    buffer = buffer[index:]

                if len(buffer) >= self.byte_length:
                    payload = buffer[len(self.start_bytes):self.byte_length]
                    buffer = buffer[self.byte_length:]

                    if len(payload) % 2 != 0:
                        payload = payload[:-1]
                    data = struct.unpack(f'<{len(payload)//2}H', payload)
                    data = data[::-1]

                    data_in_uint16.extend([data])
                else:
                    break
        data_in_uint16 = np.array(data_in_uint16)
        return data_in_uint16.mean(axis=0)

    def read_data(self, number_of_instances):
        ys = self.read_from_device(number_of_instances)
        print(ys)
        ys = -1 * (ys - 4096)

        xs = np.linspace(start=0, stop=500, num=len(ys))

        value = np.array([xs, ys]).T
        return value

    def start_device(self):
        return_value = 0
        error_instances = 0
        while return_value != 2:
            return_value = self.ser.write(self.start_command)
            sleep(0.01)
            error_instances += 1
            if error_instances > 10:
                raise TimeoutError("Device not responding")

    def stop_device(self):
        return_value = 0
        error_instances = 0
        while return_value != 2:
            return_value = self.ser.write(self.stop_command)
            sleep(0.01)
            error_instances += 1
            if error_instances > 10:
                raise TimeoutError("Device not responding")
