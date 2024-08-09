import tkinter as tk
import numpy as np
from tkinter import filedialog
import threading


class ControlPanelInterface(tk.Frame):
    options = ["Intensity", "Absorption", "Transmission"]

    def __init__(self, parent, wrapper, style_dict):
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
        self.is_first_data = True
        self.dark_spectrum_button = tk.Button(self, text="Dark Spectrum", command=self.dark_spectrum,
                                              **self.style_dict["Button"])
        self.dark_spectrum_button.pack()
        self.reference_button = tk.Button(self, text="Reference Spectrum", command=self.ref_button,
                                          **self.style_dict["Button"])
        self.reference_button.pack()
        self.load_button = tk.Button(self, text="Load", command=self.load_func, **self.style_dict["Button"])
        self.load_button.pack()
        self.DetectSolution = tk.Button(self, text="Detect Solution", **self.style_dict["Button"],
                                        command=self.detect_solution)
        self.DetectSolution.pack()
        self.save_button = tk.Button(self, text="Save", command=self.save, **self.style_dict["Button"])
        self.save_button.pack()
        self.Dark_spectrum_data = np.array([])
        self.restrict_data = np.array([])
        self.add_listener_()
        self.var = None

    @staticmethod
    def saves_file_path():
        return tk.filedialog.asksaveasfilename(
            title="Give a .csv file name",
            filetypes=[("Only csv files", "*.csv")]
        )

    def save(self):
        path = filedialog.asksaveasfilename(
            title="Give a .csv file name",
            filetypes=[("Only csv files", "*.csv")]
        )
        data_frame = self.wrapper.graph.get_positions_frame()
        data_frame.to_csv(path, index=False)

    def detect_solution(self):
        pos = self.wrapper.graph.pos_options.get(self.selected_option)
        y_pos = pos[:, 1]
        y_pos_list = list(y_pos)

    def long_running_process_step(self):
        while self.running:
            data = self.wrapper.backend.read_data(self.AverageSlider.get())
            if self.is_first_data:
                self.wrapper.graph.dark_spectrum = np.zeros((len(data), 2))
                self.wrapper.graph.reference_spectrum = np.ones((len(data), 2))
                self.is_first_data = False

            self.wrapper.graph.set_spectre_positions(data, self.selected_option)
            self.wrapper.graph.show_graph()

    def on_choice(self):
        choice = self.var.get()
        self.selected_option = choice

    def add_listener_(self):
        self.var = tk.StringVar(value=self.options[0])
        for option in self.options:
            radio = tk.Radiobutton(self, text=option, variable=self.var, value=option, command=self.on_choice,
                                   **self.style_dict["Button"])
            radio.pack(anchor=tk.E, side=tk.TOP, pady=10)

    def toggle_process(self):
        self.start_button.config(state="disabled")

        cooldown_period = 500  # 0.5 second

        if not self.running:
            self.running = True
            self.start_button["text"] = "Stop"
            self.wrapper.backend.start_device()
            threading.Thread(target=self.long_running_process_step, daemon=True).start()
            # self.long_running_process_step()
        else:
            self.running = False
            self.start_button["text"] = "Start"
            self.wrapper.backend.stop_device()

        self.root.after(cooldown_period, lambda: self.start_button.config(state="normal"))

    def load_func(self):
        the_file = filedialog.askopenfilename(  # Open explorer
            title="Select a .csv file",
            filetypes=(("CSV Files", "*.csv"),)  # File type only csv
        )
        with open(the_file, 'r') as file:
            csv_file = file.readlines()
            self.wrapper.graph.load_graph(csv_file)

    def dark_spectrum(self):
        pos = self.wrapper.backend.read_data()
        self.wrapper.graph.set_dark_spectrum(pos)

    def ref_button(self):
        pos = self.wrapper.backend.read_data()
        self.wrapper.graph.set_reference_spectrum(pos)
