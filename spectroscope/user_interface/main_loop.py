import tkinter as tk
import json
from backend_functions import Backend
from typing import Dict
from control_panel_interface import ControlPanelInterface

class SpectroscopeUI:
    def __init__(self, style_dict: Dict):
        self.backend = Backend(port= "COM3", baudrate=9600, stopbit=1)
        self.root = tk.Tk()
        self.root.title("YSO_spectroscope")
        self.style_dict = style_dict
        self.control_panel = ControlPanelInterface(self.root,self , self.style_dict).place(relx=0.7, relwidth=0.3, relheight=1.0)

if __name__ == "__main__":

    with open("default_style.json", "r") as f:
        style_dict = json.load(f)
    spectroscope = SpectroscopeUI(style_dict)

    # Helper method for processing the choice of a radio button.

    # def on_option_change(option):
    #     print(f"Option changed to: {option}")

    spectroscope.root.mainloop()
