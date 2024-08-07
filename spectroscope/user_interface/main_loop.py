import tkinter as tk
import json
from backend_functions import Backend
from typing import Dict


class SpectroscopeUI:
    def __init__(self, style_dict: Dict):
        self.backend = Backend(port= "COM3", baudrate=9600, stopbit=1)
        self.root = tk.Tk()
        self.root.title("YSO_spectroscope")
        self.style_dict = style_dict


from GraphInterface import GraphInterface

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YSO_spectroscope")
    # with open("default_style.json", "r") as f:
    #     style_dict = json.load(f)
    spectroscope = SpectroscopeUI(style_dict)

    coordinate = [(400, 4), (500, 7), (600, 12), (700, 5)]

    graph_frame = tk.Frame(root)
    graph_frame.place(relwidth=0.7, relheight=1.0)
    grap = GraphInterface(root, graph_frame)

    button_frame = tk.Frame(root, bg='green')
    button_frame.place(relx=0.7, relwidth=0.3, relheight=1.0)
    grap.SetSpectrePositions(coordinate)
    grap.ShowGraph()

    spectroscope.root.mainloop()
