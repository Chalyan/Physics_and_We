import tkinter as tk
from tkinter import ttk

class ControlPanelInterface(tk.Frame):
    global options
    options= ["Intensity", "Absorbance", "Transmittance"]
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg = "green")
        self.root = parent
        self.style_dict = style_dict
        self.combo = (ttk.Combobox(parent, values=options))
        self.combo.place(relx=0.7)
        self.combo.set(options[0])




