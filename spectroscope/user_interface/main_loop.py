import tkinter as tk
import json
from backend_functions import Backend
from typing import Dict
from control_panel_interface import ControlPanelInterface
from GraphInterface import GraphInterface
import numpy as np


class SpectroscopeUI:
    def __init__(self, style_dict: Dict):
        self.backend = Backend(port="COM3", baudrate=9600, stopbit=1)
        self.root = tk.Tk()
        self.root.title("YSO_spectroscope")
        self.style_dict = style_dict
        self.control_panel = (ControlPanelInterface(self.root, self , self.style_dict))
        self.control_panel.place(relx=0.7, relwidth=0.3, relheight=1.0)
        graph_frame = tk.Frame(self.root)
        self.graph = GraphInterface(self.root, self,graph_frame)
        self.graph.graph_frame.place(relwidth=0.7, relheight=1.0)

        # Initialize the control panel interface and pass the backend to it
        self.control_panel = ControlPanelInterface(self.root,self , self.style_dict)
        self.control_panel.place(relx=0.7, relwidth=0.3, relheight=1.0)

if __name__ == "__main__":
    with open("default_style.json", "r") as f:
        style_dict = json.load(f)
    spectroscope = SpectroscopeUI(style_dict)
    custom_data = np.array([
        [1, 10],
        [2, 20],
        [3, 15],
        [4, 25],
        [5, 30],
        [6, 18],
        [7, 22],
        [8, 28],
        [9, 24],
        [10, 30]
    ])

    dark_spectrum = np.array([[pos[0], pos[1] - 2] for pos in custom_data])
    spectroscope.graph.set_dark_spectrum(dark_spectrum)

    reference_spectrum = np.array([[pos[0], pos[1] - 2] for pos in custom_data])
    spectroscope.graph.set_reference_spectrum(reference_spectrum)

    spectroscope.graph.set_spectre_positions(custom_data, spectroscope.control_panel.selected_option)
    spectroscope.graph.show_graph()



    # Helper method for processing the choice of a radio button.

    # def on_option_change(option):
    #     print(f"Option changed to: {option}")

    spectroscope.root.mainloop()
