import csv
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np

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
        self.transmittance_pos[:, 1] = np.log(1 - self.intensity_pos[:, 1] / self.reference_spectrum[:, 1])

    def calculate_absorbance_pos(self):
        self.absorbance_pos[:, 1] = np.log(self.intensity_pos[:, 1] / self.reference_spectrum[:, 1])

    def calculate_intensity_pos(self):
        self.intensity_pos[:, 1] -= self.dark_spectrum[:, 1]

    def set_dark_spectrum(self, noise: np.ndarray):
        self.dark_spectrum = noise

    def get_reference_spectrum(self, refNoise: np.ndarray):
        self.reference_spectrum = refNoise
        self.reference_spectrum[:, 1] -= self.dark_spectrum[:, 1]

    def get_positions_csv(self):
        return pd.DataFrame(self.coordinate)

    def load_graph(self, csv_file: str):
        self.coordinate = self.csv_to_numpy_array(csv_file)
        self.show_graph()

    def csv_to_numpy_array(self, file_path: str):
        data = np.loadtxt(file_path, delimiter=',', dtype=int)
        return data

    def show_graph(self):
        x_point = self.intensity_pos[:, 0]
        y_point = self.intensity_pos[:, 1]

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(x_point, y_point)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
