# 15) Open Files Dialog Box - Python Tkinter GUI Tutorial

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Open files in dialog box")


def open():
    global img
    root.filename = filedialog.askopenfilename(
        initialdir=r"C:\Users\31IN\Desktop\Study material\python\GUI python tkinter\pics",
        title="Select a file",
        filetypes=(
            ("Png files", "*.png"),
            ("Ico files", "*.ico"),
            ("All files", "*.*"),
        ),
    )
    lb = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    lb = Label(root, image=img).pack()


btn = Button(root, text="Open file", command=open).pack()

root.mainloop()
