# 16) Sliders With TKinter - Python Tkinter GUI Tutorial

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Sliders")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=100)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()

root.mainloop()
