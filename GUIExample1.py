import tkinter as tk

# To create a main window
window = tk.Tk()
window.title("Sample Program")

# To create a label
label1 = tk.Label(window, text="Hello")
label1.pack()

window.mainloop()