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
        self.start_command = b'0xa0b0'
        self.stop_command = b'0xa1b1'
        self.start_bytes = b'0xffa0'
        self.wrapper = wrapper

    def read_data1(self, number_of_instances):
        custom_data = np.array([(i, random.randint(1, 480)) for i in range(1, 500)])
        custom_data1 = np.array([
            [457.21, 8779.584],
            [457.80, 8895.733],
            [458.38, 9010.885],
            [458.96, 9126.944],
            [459.55, 9238.880],
            [460.13, 9352.736],
            [460.71, 9458.473],
            [461.30, 9564.340],
            [461.88, 9670.698],
            [462.46, 9769.005],
            [463.05, 9868.751],
            [463.63, 9963.769],
            [464.21, 10057.045],
            [464.79, 10154.188],
            [465.38, 10250.243],
            [465.96, 10344.663],
            [466.54, 10438.102],
            [467.13, 10532.271],
            [467.71, 10622.635],
            [468.29, 10713.082],
            [468.87, 10796.979],
            [469.46, 10882.715],
            [470.04, 10963.223],
            [470.62, 11043.936],
            [471.21, 11120.855],
            [471.79, 11188.895],
            [472.37, 11258.880],
            [472.95, 11322.631],
            [473.54, 11379.203],
            [474.12, 11429.567],
            [474.70, 11474.739],
            [475.28, 11514.791],
            [475.87, 11543.533],
            [476.45, 11566.325],
            [477.03, 11581.378],
            [477.61, 11590.911],
            [478.19, 11596.783],
            [478.78, 11595.855],
            [479.36, 11584.338],
            [479.94, 11574.554],
            [480.52, 11552.802],
            [481.11, 11525.042],
            [481.69, 11496.386],
            [482.27, 11458.853],
            [482.85, 11423.938],
            [483.43, 11384.009],
            [484.01, 11340.806],
            [484.60, 11298.320],
            [485.18, 11256.148],
            [485.76, 11209.428],
            [486.34, 11163.289],
            [486.92, 11113.509],
            [487.51, 11064.299],
            [488.09, 11014.469],
            [488.67, 10956.881],
            [489.25, 10907.919],
            [489.83, 10854.484],
            [490.41, 10799.523],
            [490.99, 10744.871],
            [491.58, 10686.983],
            [492.16, 10628.404],
            [492.74, 10566.282],
            [493.32, 10505.317],
            [493.90, 10437.386],
            [494.48, 10376.872],
            [495.06, 10310.115],
            [495.64, 10243.312],
            [496.23, 10172.438],
            [496.81, 10104.526],
            [497.39, 10038.534],
            [497.97, 9969.796],
            [498.55, 9905.130],
            [499.13, 9838.897],
            [499.71, 9774.132],
            [500.29, 9705.678],
            [500.87, 9637.301],
            [501.45, 9574.701],
            [502.03, 9513.159],
            [502.61, 9453.005],
            [503.20, 9388.819],
            [503.78, 9330.105],
            [504.36, 9269.427],
            [504.94, 9213.487],
            [505.52, 9157.390],
            [506.10, 9099.154],
            [506.68, 9040.371],
            [507.26, 8986.088],
            [507.84, 8928.034]
        ])

        return custom_data1

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
