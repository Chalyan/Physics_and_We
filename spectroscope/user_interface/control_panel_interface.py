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
        self._radiobutton_observers = []
        self._selected_option = None

    def add_listener_(self):
        self.var = tk.StringVar(value=options[0])

        for option in options:
            radio = tk.Radiobutton(self.root, text=option, variable=self.var, value=option, command=self.on_choice)
            radio.pack(anchor=tk.E)

    @property
    def selected_option(self):
        return self._selected_option

    @selected_option.setter
    def selected_option(self, value):
        self._selected_option = value
        for callback in self._radiobutton_observers:
            print(value)
            callback(self._selected_option)

    def on_choice(self):
        choice = self.var.get()
        self.selected_option(choice)


    def bind_to(self, callback):
        self._radiobutton_observers.append(callback)

