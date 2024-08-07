import tkinter as tk


class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg = "blue")
        self.root = parent
        self.style_dict = style_dict
        self.AverageSlider = tk.Scale(self, from_=1, to=100,
                                      **self.style_dict["Scale"])
        self.AverageSlider.pack()

