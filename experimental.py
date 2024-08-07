import tkinter as tk
import time


class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg="green")
        self.root = parent
        self.style_dict = style_dict

        # Initialize the button in an inactive state
        self.measure_button = tk.Button(self, text="Measure Once", command=self.start_device, state=tk.DISABLED)
        self.measure_button.pack(padx=20, pady=20)

        # Label to show status messages
        self.status_label = tk.Label(self, text="Waiting for background measurement...", relief=tk.SUNKEN, anchor="w")
        self.status_label.pack(padx=20, pady=5, fill=tk.X)

        # Start the background measurement process
        self.measure_background()

    def measure_background(self):
        # Simulate background measurement
        self.update_status("Measuring background...")
        self.root.update()  # Ensure GUI updates immediately
        time.sleep(2)  # Simulate delay for measurement

        # After measuring the background, activate the button
        self.measure_button.config(state=tk.NORMAL)
        self.update_status("Background measurement complete. Button activated.")

    def start_device(self):
        # Disable the button to prevent further clicks
        self.measure_button.config(state=tk.DISABLED)

        # Simulate sending start command to the device
        self.update_status("Sending start command to device...")
        self.root.update()  # Ensure GUI updates immediately
        print("Sending start command to device...")
        # Here you would actually send a start command to your device

        # Simulate waiting to collect data
        time.sleep(5)  # Simulate data collection time

        # Simulate sending stop command to the device
        self.update_status("Sending stop command to device...")
        self.root.update()  # Ensure GUI updates immediately
        print("Sending stop command to device...")
        # Here you would actually send a stop command to your device

        # Update the status label to indicate completion
        self.update_status("Data collection complete. Device stopped.")

    def update_status(self, message):
        # Update the status label with the given message
        self.status_label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    style_dict = {}  # Dummy style_dict, adjust as needed
    panel = ControlPanelInterface(root, style_dict)
    panel.pack(fill="both", expand=True)
    root.mainloop()
