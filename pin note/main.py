import tkinter as tk
from datetime import datetime
import pytz
import time

def cli():
    current_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%H:%M")

    print("Welcome to Pin Your Note Application.")
    time.sleep(2)
    note_input = input("Type your notes here: ")
    note = ("%s") % note_input
    time.sleep(1)

    root = tk.Tk()
    root.title("Pin Your Note")
    root.geometry("300x300")

    tk.Label(root, text=current_time).pack()
    tk.Label(root, text=note).pack()

    root.mainloop()

cli()
