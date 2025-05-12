import tkinter as tk
from tkinter import messagebox

def show_dialog():
    messagebox.showinfo("Dialog Box", "This is a dialog box")

window = tk.Tk()
window.title("Example 3")

button = tk.Button(window, text="Show Dialog", command=show_dialog)
button.pack()

window.mainloop()