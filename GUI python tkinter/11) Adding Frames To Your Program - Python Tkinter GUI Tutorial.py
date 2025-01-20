# 11) Adding Frames To Your Program - Python Tkinter GUI Tutorial

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("This window")

# Until frames were introduced, we can only use one positioning method throughout the tkinter pgm (i.e) either pack or grid. But by using frames we can use them simultaneously. It's somewhat similar to span in html.

# frame = LabelFrame(root, text="This is a frame.......", padx = 50, pady = 50)
frame = LabelFrame(root, padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10)

b1 = Button(frame, text="This button1 is inside the frame")
# b1.pack()
b1.grid(row=0, column=0, padx = 10, pady = 10) # without frames this line would cause an error

b2 = Button(frame, text="This button2 is inside the frame")
# b2.pack()
b2.grid(row=1, column=0, padx = 10, pady = 10) # without frames this line would cause an error


root.mainloop()
