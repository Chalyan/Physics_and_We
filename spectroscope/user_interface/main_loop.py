import tkinter as tk
import json

from GraphInterface import GraphInterface

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YSO_spectroscope")
    # with open("default_style.json", "r") as f:
    #     style_dict = json.load(f)

    coordinate = [(400, 4), (500, 7), (600, 12), (700, 5)]

    graph_frame = tk.Frame(root)
    graph_frame.place(relwidth=0.7, relheight=1.0)
    grap = GraphInterface(root, graph_frame)

    button_frame = tk.Frame(root, bg='green')
    button_frame.place(relx=0.7, relwidth=0.3, relheight=1.0)
    grap.SetSpectrePositions(coordinate)
    grap.ShowGraph()

    root.mainloop()
