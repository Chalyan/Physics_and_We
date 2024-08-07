import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphInterface:
    def __init__(self, root, graph_frame):
        self.root = root
        self.graph_frame = graph_frame

    def SetSpectrePositions(self, coord: list[float]):
        self.coordinate = coord

    def ShowGraph(self):
        x_point = [coord[0] for coord in self.coordinate]
        y_point = [coord[1] for coord in self.coordinate]

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        ax.plot(x_point, y_point)
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
