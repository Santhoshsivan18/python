# 14) Create New Windows in tKinter - Python Tkinter GUI Tutorial

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Create new window in tkinter")


def open():
    global img  # If the img variable is not declared as global, python automatic garbage collector collects it & disposes as garbage
    top = Toplevel(root)
    top.title("This is a new window")
    lb = Label(top, text="Hello world").pack()
    img = ImageTk.PhotoImage(Image.open(r"GUI python tkinter\paper.png"))
    lb = Label(top, image=img).pack()
    b2 = Button(top, text="Close the 2nd window", command=top.destroy).pack()


button = Button(root, text="Open second window", command=open).pack()

root.mainloop()
