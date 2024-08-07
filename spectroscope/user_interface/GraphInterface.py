import csv
import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class GraphInterface(tk.Frame):
    def __init__(self, parent, graph_frame):
        tk.Frame.__init__(self, parent, graph_frame)
        self.parent = parent
        self.graph_frame = graph_frame
        self.canvas = None

    def setSpectrePositions(self, coord):
        self.coordinate = coord
        index = 0
        for y in self.coordinate:
            y_list = list(y)
            y_list[1] -= self.backgroundNoise
            self.coordinate[index] = tuple(y_list)
            index += 1

    def setBackgrounNoise(self, backNoise: int):
        self.backgroundNoise = backNoise

    def getPositionsCsv(self):
        return pd.DataFrame(self.coordinate)

    def loadGraph(self, csv_file: str):
        self.coordinate = self.csv_to_list_of_tuples(csv_file)
        self.showGraph()

    def csv_to_list_of_tuples(self, file_path: str):
        list_of_tuples = []

        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                list_of_tuples.append((int(row[0]), int(row[1])))

        return list_of_tuples

    def showGraph(self):
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
