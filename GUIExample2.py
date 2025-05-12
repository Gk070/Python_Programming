import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Example 2")

# Open image file
image_obj = Image.open("img.jpg")
k = (200, 100)
image_obj = image_obj.resize(k)

# Create an image tk
image_tk = ImageTk.PhotoImage(image_obj)

label1 = tk.Label(window, image = image_tk)
label1.pack()

window.mainloop()