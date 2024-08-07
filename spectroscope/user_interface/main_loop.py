import tkinter as tk
import json

from GraphInterface import GraphInterface

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YSO_spectroscope")
    # with open("default_style.json", "r") as f:
    #     style_dict = json.load(f)

    coordinate = [(400, 4), (500, 7), (600, 12), (700, 5)]
    grap = GraphInterface(root)
    grap.SetSpectrePositions(coordinate)
    grap.ShowGraph()

    root.mainloop()
