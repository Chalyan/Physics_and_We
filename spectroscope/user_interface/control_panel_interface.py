import tkinter as tk
from tkinter import filedialog
import os
import csv

class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg = "green")
        self.root = parent
        self.style_dict = style_dict
        self.save_button = tk.Button(self.root, text = "Browse Files", command = self.save)
        self.save_button.pack()
    
    def saves_file_path(self):
        return filedialog.asksaveasfilename(  
            title = "Give a .csv file name",  
            filetypes = [("Only csv files", "*.csv")]  
            )
    
    def save(self, data_frame):
        path = filedialog.asksaveasfilename(  
            title = "Give a .csv file name",  
            filetypes = [("Only csv files", "*.csv")]  
            )
        data_frame.to_csv(path, index=False)



