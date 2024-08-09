import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np


class GraphInterface(tk.Frame):
    def __init__(self, parent, wrapper, graph_frame):
        tk.Frame.__init__(self, parent, graph_frame)
        self.parent = parent
        self.wrapper = wrapper
        self.graph_frame = graph_frame
        self.canvas = None
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.intensity_pos = None
        self.absorbance_pos = None
        self.transmittance_pos = None
        self.dark_spectrum = None
        self.reference_spectrum = None

    def set_spectre_positions(self, coord, option: str):
        self.intensity_pos = coord
        self.calculate_intensity_pos()
        if option == "Intensity":
            return
        if option == "Absorption":
            self.absorbance_pos = coord
            self.calculate_absorbance_pos()
            return
        if option == "Transmission":
            self.transmittance_pos = coord
            self.calculate_transmittance_pos()

    def get_pos_options(self, option):
        option = self.wrapper.control_panel.selected_option
        pos_options = {
            "Intensity": self.intensity_pos,
            "Absorption": self.absorbance_pos,
            "Transmission": self.transmittance_pos
        }
        return pos_options.get(option)

    def calculate_transmittance_pos(self):
        self.transmittance_pos[:, 1] = np.log(1 - self.intensity_pos[:, 1] / self.reference_spectrum[:, 1])

    def calculate_absorbance_pos(self):
        self.absorbance_pos[:, 1] = np.log(self.intensity_pos[:, 1] / self.reference_spectrum[:, 1])

    def calculate_intensity_pos(self):
        self.intensity_pos[:, 1] = self.intensity_pos[:, 1].astype(np.float64) - self.dark_spectrum[:, 1]

    def set_dark_spectrum(self, noise: np.ndarray):
        self.dark_spectrum = noise

    def set_reference_spectrum(self, ref_noise: np.ndarray):
        self.reference_spectrum = ref_noise
        # self.reference_spectrum[:, 1] -= self.dark_spectrum[:, 1]

    def get_positions_frame(self):
        option = self.wrapper.control_panel.selected_option
        pos_options = {
            "Intensity": self.intensity_pos,
            "Absorption": self.absorbance_pos,
            "Transmission": self.transmittance_pos
        }
        pos = pos_options.get(option)
        header = ["WaveLength Nm", option]

        data_with_header = np.vstack([header, pos])

        return pd.DataFrame(data_with_header)

    def load_graph(self, csv_file: str):
        parts = csv_file[1].split(',')
        second_word = parts[1] if len(parts) > 1 else None

        word = second_word[:-1]
        self.wrapper.control_panel.selected_option = word
        self.wrapper.control_panel.var.set(word)
        data = [line.strip() for line in csv_file[2:]]

        float_data = [list(map(float, line.split(','))) for line in data]

        array = np.array(float_data)
        self.show_graph_pos(array)

    @staticmethod
    def csv_to_numpy_array(file_path: str):
        data = np.loadtxt(file_path, delimiter=',', dtype=int)
        return data

    def show_graph(self):
        pos_options = {
            "Intensity": self.intensity_pos,
            "Absorption": self.absorbance_pos,
            "Transmission": self.transmittance_pos
        }
        option = self.wrapper.control_panel.selected_option
        pos = pos_options.get(option)
        x_point = pos[:, 0]
        y_point = pos[:, 1]
        if self.ax:
            self.ax.clear()

        self.ax.plot(x_point, y_point)

        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_graph_pos(self, pos):
        x_point = pos[:, 0]
        y_point = pos[:, 1]

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(x_point, y_point)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
