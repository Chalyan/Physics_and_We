import tkinter as tk
import json
from backend_functions import Backend
from typing import Dict
from control_panel_interface import ControlPanelInterface
from GraphInterface import GraphInterface


class SpectroscopeUI:
    def __init__(self, style_dict: Dict):
        self.backend = Backend(port="COM3", baudrate=9600, wrapper=self)
        self.root = tk.Tk()
        self.root.geometry("1450x1000")
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

    spectroscope.root.mainloop()
