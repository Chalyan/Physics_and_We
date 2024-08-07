import tkinter as tk


class ControlPanelInterface(tk.Frame):
    def __init__(self, parent, style_dict):
        tk.Frame.__init__(self, parent, bg = "green")
        self.root = parent
        self.style_dict = style_dict

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






