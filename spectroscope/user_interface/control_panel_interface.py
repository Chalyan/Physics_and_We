import tkinter as tk


class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        self.parent = parent
        self.style_dict = style_dict

