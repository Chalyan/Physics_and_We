import tkinter as tk
import threading



class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict
        self.start_button = tk.Button(self, text="Start", command=self.toggle_process )
        self.start_button.pack()
        self.measure_once_button=tk.Button(self, text="Measure once", command=self.start_device, state=tk.DISABLED)
        self.measure_once_button.pack(padx=200,pady=20)

        self.status_label= tk.Label(self,text="Waiting for background measurement...",relief=tk.SUNKEN,anchor="w")
        self.status_label.pack(padx=20,pady=5,fill=tk.X)
        self.measure_background()

    def measure_background(self):
        self.status_label.config(text="Measuring background...")
        self.update()

        self.status_label.config(text="Background measurement complete.")
        self.measure_once_button.config(state=tk.NORMAL)
        self.running = False

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
