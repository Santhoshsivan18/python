# 12) Radio Buttons with TKinter - Python Tkinter GUI Tutorial

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Radio buttons")

# r = IntVar()

MODES = [
    ("Apple", "Apple"),
    ("Banana", "Banana"),
    ("Grapes", "Grapes"),
    ("Orange", "Orange"),
]

fruit = StringVar()
fruit.set("Apple")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=fruit, value=mode).pack()


def click(val):
    my_label = Label(root, text=val).pack()


# r = StringVar()
# Radiobutton(root, text="Option 1", variable=r, value="1").pack()

# r1 = Radiobutton(root, text="Option 1", variable=r, value=1).pack()
# r2 = Radiobutton(root, text="Option 2", variable=r, value=2).pack()

my_button = Button(root, text="Click me!!", command=lambda: click(fruit.get())).pack()

root.mainloop()

# 150 - 1 month
# 440 - 3 months