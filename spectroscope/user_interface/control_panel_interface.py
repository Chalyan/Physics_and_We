import tkinter as tk
from tkinter import ttk

class ControlPanelInterface(tk.Frame):
    global options
    options= ["Intensity", "Absorbance", "Transmittance"]
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.add_listener_()
        self._observers = []

    def add_listener_(self):
        self.var = tk.StringVar(value=options[0])

        for option in options:
            radio = tk.Radiobutton(self.root, text=option, variable=self.var, value=option, command=self.on_choice)
            radio.pack(anchor=tk.E)

    def on_choice(self):
        selected_option = self.var.get()
        print(f"Selected option: {selected_option}")
        for callback in self._observers:
            callback(selected_option)

    def bind_to(self, callback):
        self._observers.append(callback)

