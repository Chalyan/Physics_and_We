import tkinter as tk
import threading

class ControlPanelInterface(tk.Frame):
    options = ["Intensity", "Absorption", "Transmission"]
    def __init__(self, parent, wrapper,style_dict):
        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.wrapper = wrapper
        self.add_listener_()
        self.selected_option = self.options[0]
        self.AverageSlider = tk.Scale(self, from_=1, to=100,
                                      **self.style_dict["Scale"])
        self.AverageSlider.pack()
        self.start_button = tk.Button(self, text="Start", command=self.toggle_process )
        self.start_button.pack()
        self.running = False


    def long_running_process(self):
        while self.running:
            print("..........")

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
