import tkinter as tk
from tkinter import filedialog
import csv

class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg = "green")
        self.parent = parent
        self.style_dict = style_dict
        self.load_button = tk.Button(self, text="Load", command=self.load_func)
        self.load_button.pack()

    def load_func(self):
        the_file = filedialog.askopenfilename(  # Open explorer
            title = "Select a .csv file",  
            filetypes = (("CSV Files","*.csv"),) # File type only csv
            )  
        with open(the_file, 'r') as csv_file:
            file = csv_file.readlines()
        return file            






