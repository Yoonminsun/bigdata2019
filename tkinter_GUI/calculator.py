import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

for i in range(3):
    for j in range(3):
        num_button = ttk.Button(root,text="%d"%(((i*3))+j+1))
        num_button.grid(row=i, column=j+1)


root.mainloop()
