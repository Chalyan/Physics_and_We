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


if __name__ == "__main__":

    with open("default_style.json", "r") as f:
        style_dict = json.load(f)
    spectroscope = SpectroscopeUI(style_dict)

    spectroscope.root.mainloop()
