# 8) Using Icons, Images and Exit Buttons - Python Tkinter GUI Tutorial

from tkinter import *
# to use imgs -> goto terminal -> "pip install Pillow" - download & install python img library. PIL->Pillow
# Supported file types : png,jpeg
from PIL import ImageTk, Image

root = Tk()
root.title("Using icons,img and exit buttons")

# iconbitmap - set a custom icon for the main window of a Tkinter app. Supported file types : ico


# root.iconbitmap("C:\Users\31IN\Desktop\Study material\python\GUI python tkinter\pyramid.ico") - error for not using double backslash

# root.iconbitmap("C:\\Users\\31IN\\Desktop\\Study material\\python\\GUI python tkinter\\pyramid.ico")

root.iconbitmap(r"GUI python tkinter\pyramid.ico")

# Adding imgs in tkinter 3 steps - defining, loading, displaying
my_img = ImageTk.PhotoImage(Image.open(r"GUI python tkinter\paper.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit button", command=root.quit)
button_quit.pack()

root.mainloop()