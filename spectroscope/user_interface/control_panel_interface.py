import tkinter as tk
import os
import csv
import threading
from tkinter import filedialog
import csv

class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, wrapper,style_dict):

        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.wrapper = wrapper
        self.AverageSlider = tk.Scale(self, from_=1, to=100,
                                      **self.style_dict["Scale"])
        self.AverageSlider.pack()
        self.start_button = tk.Button(self, text="Start", command=self.toggle_process )
        self.start_button.pack()
        self.running = False  # Assume the process is not running at the beginning
        self.status_label= tk.Label(self,text="Waiting for background measurement...",relief=tk.SUNKEN,anchor="w")
        self.status_label.pack(padx=20,pady=5,fill=tk.X)
        self.load_button = tk.Button(self, text="Load", command=self.load_func)
        self.load_button.pack()
        self.save_button = tk.Button(self, text = "Save", command = self.save)
        self.save_button.pack()
    
    def saves_file_path(self):
        return tk.filedialog.asksaveasfilename(  
            title = "Give a .csv file name",  
            filetypes = [("Only csv files", "*.csv")]  
            )
    
    def save(self):
        path = tk.filedialog.asksaveasfilename(  
            title = "Give a .csv file name",  
            filetypes = [("Only csv files", "*.csv")]  
            )
        data_frame = self.wrapper.graph.get_positions_frame()
        data_frame.to_csv(path, index=False)


    def long_running_process(self):
        while self.running:
            print("..........")

    #  start or stop the process
    def toggle_process(self):

        # Disable the button
        self.start_button.config(state="disabled")

        # Cooldown
        cooldown_period = 500  # 0.5 second

        if not self.running:
            self.running = True  # Start the process
            self.start_button["text"] = "Stop"
            threading.Thread(target=self.long_running_process, daemon=True).start()
        else:
            self.running = False  # Stop the process
            self.start_button["text"] = "Start"

        self.root.after(cooldown_period, lambda: self.start_button.config(state="normal"))

    #   load file
    def load_func(self): 
        the_file = filedialog.askopenfilename(  # Open explorer
            title = "Select a .csv file",  
            filetypes = (("CSV Files","*.csv"),) # File type only csv
            )  
        with open(the_file, 'r') as file: 
            csv_file = file.readlines()
            self.wrapper.graph.loadGraph(csv_file)
