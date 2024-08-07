import tkinter as tk
import threading

#  long-running process
def long_running_process():
    while running:
        print("..........")


#  start or stop the process
def toggle_process():
    global running

    # Disable the button
    start_button.config(state="disabled")

    # Cooldown
    cooldown_period = 500  # 0.5 second

    if not running:
        running = True
        start_button["text"] = "Stop"
        threading.Thread(target=long_running_process).start()
    else:
        running = False
        start_button["text"] = "Start"

    root.after(cooldown_period, lambda: start_button.config(state="normal"))


root = tk.Tk()
root.title("Start/Stop")
root.geometry("300x200")

# Create a button
start_button = tk.Button(root, text="Start", command=toggle_process)
start_button.pack()

running = False

root.mainloop()