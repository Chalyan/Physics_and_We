import tkinter as tk
import threading
import numpy as np
from backend_functions import Backend  # Update import path as necessary

class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, wrapper,style_dict):

        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.wrapper = wrapper

        self.start_button = tk.Button(self, text="Start", command=self.toggle_process)
        self.start_button.pack(pady=10)

        # Initialize save buttons (hidden initially)
        self.save_button1 = tk.Button(self, text="Save Dark Spectrum", state=tk.DISABLED,
                                      command=self.save_dark_spectrum_data)
        self.save_button2 = tk.Button(self, text="Save Reference Spectrum Data", state=tk.DISABLED,
                                      command=self.save_restrict_data)
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

        # Initialize arrays to store the data
        self.Dark_spectrum_data = np.array([])
        self.restrict_data = np.array([])

    def long_running_process(self):
        while self.running:
            data = self.graph.get_data()
            print("Acquiring data:", data)

    def toggle_process(self):
        self.start_button.config(state="disabled")

        cooldown_period = 500  # 0.5 second

        if not self.running:

            self.running = True
            self.start_button["text"] = "Stop"
            threading.Thread(target=self.long_running_process, daemon=True).start()

            self.save_button1.pack()
            self.save_button2.pack()
            self.save_button1.config(state=tk.NORMAL)
            self.save_button2.config(state=tk.NORMAL)
        else:
            self.running = False
            self.start_button["text"] = "Start"

            self.save_button1.config(state=tk.NORMAL)
            self.save_button2.config(state=tk.NORMAL)

        self.root.after(cooldown_period, lambda: self.start_button.config(state="normal"))
    def save_dark_spectrum_data(self):
        new_data = self.graph.get_data()
        self.Dark_spectrum_data = np.append(self.Dark_spectrum_data, new_data)
        print("Dark Spectrum data saved:", self.Dark_spectrum_data)

    def save_restrict_data(self):
        new_data = self.graph.get_data()
        self.restrict_data = np.append(self.restrict_data, new_data)
        print("Restrict data saved:", self.restrict_data)
    def load_func(self): 
        the_file = tk.askopenfilename(  # Open explorer
            title = "Select a .csv file",  
            filetypes = (("CSV Files","*.csv"),) # File type only csv
            )  
        with open(the_file, 'r') as file: 
            csv_file = file.readlines()
            self.wrapper.graph.loadGraph(csv_file)
