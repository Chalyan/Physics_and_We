import tkinter as tk
import json
from backend_functions import Backend
from typing import Dict
from GraphInterface import GraphInterface


class SpectroscopeUI:
    def __init__(self, style_dict: Dict):
        self.backend = Backend(port= "COM3", baudrate=9600, stopbit=1)
        self.root = tk.Tk()
        self.root.title("YSO_spectroscope")
        self.style_dict = style_dict
        graph_frame = tk.Frame(self.root)
        self.graph = GraphInterface(self.root, graph_frame)
        self.graph.graph_frame.place(relwidth=0.7, relheight=1.0)

if __name__ == "__main__":
    with open("default_style.json", "r") as f:
        style_dict = json.load(f)
    spectroscope = SpectroscopeUI({})

    coordinate = [(400, 4), (500, 7), (600, 12), (700, 5)]

    spectroscope.graph.SetSpectrePositions(coordinate)
    spectroscope.graph.ShowGraph()

    spectroscope.root.mainloop()
