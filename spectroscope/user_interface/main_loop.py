import tkinter as tk
import json

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YSO_spectroscope")
    with open("default_style.json", "r") as f:
        style_dict = json.load(f)

    root.mainloop()
