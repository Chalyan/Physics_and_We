import tkinter as tk


class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg = "green")
        self.root = parent
        self.style_dict = style_dict



