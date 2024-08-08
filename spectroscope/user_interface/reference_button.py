import tkinter as tk
import threading
from tkinter import filedialog
import csv



class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, wrapper,style_dict):

        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.wrapper = wrapper
        self.reference_button = tk.Button(self, text = "Save Reference Spectrum", command=self.ref_button)
        self.reference_button.grid()
    #   reference button
    def ref_button(self):
        self.wrapper.graph.set_reference_spectrum() # need parameter