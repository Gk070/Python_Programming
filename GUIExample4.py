import tkinter as tk

def button_click1():
    input_text = f.get()
    fa = int(input_text) * 9 / 5 + 32
    print(fa)
    label1.config(text="Celsius is : " + str(fa))

def button_click2():
    input_text = c.get()
    c = int(input_text) - 32 * 5 / 9
    print(c)
    label1.config(text="Farenheit is : " + str(c))

window = tk.Tk()
window.title("Example 4")

f = tk.Entry(window)
f.pack()

button1 = tk.Button(window, text="Convert F into C", command=button_click1)
button1.pack()

label1 = tk.Label(window, text="")
label1.pack()

c = tk.Entry(window)
c.pack()

button1 = tk.Button(window, text="Convert C into F", command=button_click2)
button1.pack()

label2 = tk.Label(window, text="")
label2.pack()

window.mainloop()