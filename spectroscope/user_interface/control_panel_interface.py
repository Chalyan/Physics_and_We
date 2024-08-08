import tkinter as tk
import threading
import numpy as np

class ControlPanelInterface(tk.Frame):
    options = ["Intensity", "Absorption", "Transmission"]
    def __init__(self, parent, wrapper,style_dict):
        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.wrapper = wrapper
        self.start_button = tk.Button(self, text="Start", command=self.toggle_process)
        self.start_button.pack(pady=10)
        self.add_listener_()
        self.selected_option = self.options[0]
        self.AverageSlider = tk.Scale(self, from_=1, to=100,
                                      **self.style_dict["Scale"])
        self.AverageSlider.pack()
        self.start_button = tk.Button(self, text="Start", command=self.toggle_process )
        self.start_button.pack()
        self.running = False
        self.load_button = tk.Button(self, text="Load", command=self.load_func)
        self.load_button.pack()

        # Initialize arrays to store the data
        self.Dark_spectrum_data = np.array([])
        self.restrict_data = np.array([])

    def long_running_process(self):
        while self.running:
            data = self.wrapper.backend.read_data1(self.AverageSlider.get())

    def on_choice(self):
        choice = self.var.get()
        self.selected_option = choice
        self.wrapper.graph.calculate_position()

    def add_listener_(self):
        self.var = tk.StringVar(value=self.options[0])
        i = 0
        for option in self.options:
            radio = tk.Radiobutton(self.root, text=option, variable=self.var, value=option, command=self.on_choice)
            radio.pack(anchor=tk.E, side=tk.TOP, pady=10)

    def toggle_process(self):
        self.start_button.config(state="disabled")

        cooldown_period = 500  # 0.5 second

        if not self.running:

            self.running = True
            self.start_button["text"] = "Stop"
            threading.Thread(target=self.long_running_process, daemon=True).start()

        else:
            self.running = False
            self.start_button["text"] = "Start"


        self.root.after(cooldown_period, lambda: self.start_button.config(state="normal"))

    def load_func(self): 
        the_file = tk.askopenfilename(  # Open explorer
            title = "Select a .csv file",  
            filetypes = (("CSV Files","*.csv"),) # File type only csv
            )  
        with open(the_file, 'r') as file: 
            csv_file = file.readlines()
            self.wrapper.graph.loadGraph(csv_file)
