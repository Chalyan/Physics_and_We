import csv
import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import math


class GraphInterface(tk.Frame):
    def __init__(self, parent, graph_frame):
        tk.Frame.__init__(self, parent, graph_frame)
        self.parent = parent
        self.graph_frame = graph_frame
        self.canvas = None

    def set_spectre_positions(self, coord, index: int):
        self.intensity_pos = coord
        self.calculate_intensity_pos()
        if index == 0:
            return
        if index == 1:
            self.absorbance_pos = coord
            self.calculate_absorbance_pos()
            return
        if index == 2:
            self.transmittance_pos = coord
            self.calculate_transmittance_pos()


    def calculate_transmittance_pos(self):
        i = 0
        for y in self.transmittance_pos:
            y_list = list(y)
            y_list[1] = math.log(1 - self.intensity_pos[i] / self.reference_spectrum)
            self.transmittance_pos[i] = tuple(y_list)
            i += 1

    def calculate_absorbance_pos(self):
        i = 0
        for y in self.absorbance_pos:
            y_list = list(y)
            y_list[1] = math.log(self.intensity_pos[i] / self.reference_spectrum)
            self.absorbance_pos[i] = tuple(y_list)
            i += 1

    def calculate_intensity_pos(self):
        i = 0
        for y in self.intensity_pos:
            y_list = list(y)
            y_list[1] -= self.dark_spectrum
            self.intensity_pos[i] = tuple(y_list)
            i += 1

    def set_dark_spectrum(self, noise: float):
        self.dark_spectrum = noise

    def get_reference_spectrum(self, refNoise: float):
        self.reference_spectrum = refNoise

    def get_positions_csv(self):
        return pd.DataFrame(self.coordinate)

    def load_graph(self, csv_file: str):
        self.coordinate = self.csv_to_list_of_tuples(csv_file)
        self.show_graph()

    def csv_to_list_of_tuples(self, file_path: str):
        list_of_tuples = []

        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                list_of_tuples.append((int(row[0]), int(row[1])))

        return list_of_tuples

    def show_graph(self):
        x_point = [coord[0] for coord in self.coordinate]
        y_point = [coord[1] for coord in self.coordinate]

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(x_point, y_point)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
