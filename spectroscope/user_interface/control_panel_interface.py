import csv
import tkinter as tk
import numpy as np
from tkinter import filedialog


class ControlPanelInterface(tk.Frame):
    options = ["Intensity", "Absorption", "Transmission"]
    def __init__(self, parent, wrapper ,style_dict):
        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.wrapper = wrapper
        self.start_button = tk.Button(self, text="Start", command=self.toggle_process, **self.style_dict["Button"])
        self.start_button.pack(pady=10)
        self.selected_option = self.options[0]
        self.AverageSlider = tk.Scale(self, from_=1, to=100,
                                      **self.style_dict["Scale"])
        self.AverageSlider.pack()
        self.running = False
        self.load_button = tk.Button(self, text="Load", command=self.load_func,**self.style_dict["Button"])
        self.load_button.pack()
        self.DetectSolution = tk.Button(self, text="Detect Solution",**self.style_dict["Button"] ,command=self.detect_solution)
        self.DetectSolution.pack()
        self.save_button = tk.Button(self, text = "Save", command=self.save,**self.style_dict["Button"])
        self.save_button.pack()
        self.Dark_spectrum_data = np.array([])
        self.restrict_data = np.array([])
        self.add_listener_()
    
    def saves_file_path(self):
        return tk.filedialog.asksaveasfilename(  
            title = "Give a .csv file name",  
            filetypes = [("Only csv files", "*.csv")]  
            )
    
    def save(self):
        path = filedialog.asksaveasfilename(
            title="Give a .csv file name",
            filetypes=[("Only csv files", "*.csv")]
            )
        data_frame = self.wrapper.graph.get_positions_frame()
        data_frame.to_csv(path, index=False)

    def test_ds_rs(self):
        custom_data = np.array([
            [457.21, -9.716],
            [457.80, -9.692],
            [458.38, -9.598],
            [458.96, -9.736],
            [459.55, -9.860],
            [460.13, -10.310],
            [460.71, -9.974],
            [461.30, -10.394],
            [461.88, -10.363],
            [462.46, -11.554],
            [463.05, -11.309],
            [463.63, -11.764],
            [464.21, -11.530],
            [464.79, -11.219],
            [465.38, -10.628],
            [465.96, -10.322],
            [466.54, -10.022],
            [467.13, -9.707],
            [467.71, -9.809],
            [468.29, -9.303],
            [468.87, -9.419],
            [469.46, -9.891],
            [470.04, -10.034],
            [470.62, -9.694],
            [471.21, -8.869],
            [471.79, -9.471],
            [472.37, -9.560],
            [472.95, -9.659],
            [473.54, -9.600],
            [474.12, -9.994],
            [474.70, -10.143],
            [475.28, -10.593],
            [475.87, -10.604],
            [476.45, -10.772],
            [477.03, -10.919],
            [477.61, -10.119],
            [478.19, -10.096],
            [478.78, -9.834],
            [479.36, -10.049],
            [479.94, -10.152],
            [480.52, -10.081],
            [481.11, -9.497],
            [481.69, -9.633],
            [482.27, -9.309],
            [482.85, -9.666],
            [483.43, -10.091],
            [484.01, -9.917],
            [484.60, -10.426],
            [485.18, -10.287],
            [485.76, -11.106],
            [486.34, -11.430],
            [486.92, -11.154],
            [487.51, -10.843],
            [488.09, -10.891],
            [488.67, -10.782],
            [489.25, -10.878],
            [489.83, -11.118],
            [490.41, -11.034],
            [490.99, -12.047],
            [491.58, -12.211],
            [492.16, -11.538],
            [492.74, -11.268],
            [493.32, -11.003],
            [493.90, -10.806],
            [494.48, -10.096],
            [495.06, -9.768],
            [495.64, -10.148],
            [496.23, -10.811],
            [496.81, -11.120],
            [497.39, -10.509],
            [497.97, -10.319],
            [498.55, -10.496],
            [499.13, -10.903],
            [499.71, -10.563],
            [500.29, -9.772],
            [500.87, -9.428],
            [501.45, -9.198],
            [502.03, -9.066],
            [502.61, -8.466],
            [503.20, -8.239],
            [503.78, -8.826],
            [504.36, -8.149],
            [504.94, -7.476],
            [505.52, -6.528],
            [506.10, -7.082],
            [506.68, -6.737],
            [507.26, -6.976],
            [507.84, -6.280],

        ])
        # data = self.wrapper.backend.read_data1(self.AverageSlider.get())
        # print("data")
        # print(data)
        self.wrapper.graph.set_dark_spectrum(custom_data)
        # data1 = self.wrapper.backend.read_data1(3)
        # print("data 1")
        # print(data1)
        # self.wrapper.graph.set_reference_spectrum(data1)
        custom_data1 = np.array([
            [457.21, 10584.363],
            [457.80, 10758.604],
            [458.38, 10928.373],
            [458.96, 11098.354],
            [459.55, 11263.743],
            [460.13, 11434.461],
            [460.71, 11603.696],
            [461.30, 11771.111],
            [461.88, 11937.384],
            [462.46, 12092.042],
            [463.05, 12244.493],
            [463.63, 12391.158],
            [464.21, 12535.331],
            [464.79, 12686.728],
            [465.38, 12838.047],
            [465.96, 12987.465],
            [466.54, 13134.876],
            [467.13, 13284.123],
            [467.71, 13431.351],
            [468.29, 13578.503],
            [468.87, 13721.158],
            [469.46, 13865.015],
            [470.04, 14004.332],
            [470.62, 14142.855],
            [471.21, 14275.265],
            [471.79, 14409.000],
            [472.37, 14538.343],
            [472.95, 14666.468],
            [473.54, 14790.347],
            [474.12, 14908.186],
            [474.70, 15023.024],
            [475.28, 15132.915],
            [475.87, 15240.741],
            [476.45, 15341.633],
            [477.03, 15438.999],
            [477.61, 15527.793],
            [478.19, 15611.031],
            [478.78, 15684.304],
            [479.36, 15748.523],
            [479.94, 15812.705],
            [480.52, 15871.370],
            [481.11, 15925.689],
            [481.69, 15976.168],
            [482.27, 16018.665],
            [482.85, 16058.020],
            [483.43, 16092.872],
            [484.01, 16125.896],
            [484.60, 16157.889],
            [485.18, 16183.926],
            [485.76, 16208.982],
            [486.34, 16233.847],
            [486.92, 16251.822],
            [487.51, 16268.656],
            [488.09, 16285.094],
            [488.67, 16296.191],
            [489.25, 16306.871],
            [489.83, 16315.019],
            [490.41, 16318.863],
            [490.99, 16320.744],
            [491.58, 16322.429],
            [492.16, 16322.619],
            [492.74, 16321.467],
            [493.32, 16319.117],
            [493.90, 16315.747],
            [494.48, 16311.288],
            [495.06, 16307.635],
            [495.64, 16302.421],
            [496.23, 16296.911],
            [496.81, 16289.884],
            [497.39, 16283.122],
            [497.97, 16275.253],
            [498.55, 16265.842],
            [499.13, 16255.621],
            [499.71, 16244.202],
            [500.29, 16231.515],
            [500.87, 16218.022],
            [501.45, 16205.621],
            [502.03, 16192.558],
            [502.61, 16178.686],
            [503.20, 16163.736],
            [503.78, 16148.198],
            [504.36, 16133.026],
            [504.94, 16117.242],
            [505.52, 16101.158],
            [506.10, 16085.203],
            [506.68, 16069.498],
            [507.26, 16053.303],
            [507.84, 16036.600],

        ])
        self.wrapper.graph.set_reference_spectrum(custom_data1)

    def detect_solution(self):
        pos = self.wrapper.graph.pos_options.get(self.selected_option)
        y_pos = pos[:, 1]
        y_pos_list = list(y_pos)
        #minchev chpusheq chem gre exav

    def long_running_process_step(self):
        if self.running:
            # Perform one step of the long-running process
            data = self.wrapper.backend.read_data1(self.AverageSlider.get())
            self.wrapper.graph.set_spectre_positions(data, self.selected_option)
            self.wrapper.graph.show_graph()



    def on_choice(self):
        choice = self.var.get()
        self.selected_option = choice

    def add_listener_(self):
        self.var = tk.StringVar(value=self.options[0])
        i = 0
        for option in self.options:
            radio = tk.Radiobutton(self, text=option, variable=self.var, value=option, command=self.on_choice, **self.style_dict["Button"])
            radio.pack(anchor=tk.E, side=tk.TOP, pady=10)

    def toggle_process(self):
        self.test_ds_rs()
        self.start_button.config(state="disabled")

        cooldown_period = 500  # 0.5 second

        if not self.running:
            self.running = True
            self.start_button["text"] = "Stop"
            self.long_running_process_step()
        else:
            self.running = False
            self.start_button["text"] = "Start"

        self.root.after(cooldown_period, lambda: self.start_button.config(state="normal"))


    def load_func(self):
        the_file = filedialog.askopenfilename(  # Open explorer
            title="Select a .csv file",
            filetypes=(("CSV Files","*.csv"),) # File type only csv
            )  
        with open(the_file, 'r') as file: 
            csv_file = file.readlines()
            self.wrapper.graph.load_graph(csv_file)
