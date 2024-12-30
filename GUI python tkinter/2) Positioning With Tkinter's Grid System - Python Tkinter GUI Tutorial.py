# 2) Positioning With Tkinter's Grid System - Python Tkinter GUI Tutorial

# Grid sys is like matrix with rows and columns accessed using index values starting from 0
# When using the grid system, the widget positions are fixed relative to the parent window and do not resize dynamically.
# If you set a widget's row and column values to 5, but there is no content in rows and columns 1 to 4, Tkinter will ignore the empty cells and place the widget in the first available space (row 1, column 1).

# myLabel2 = Label(root, text="This is a pgm of row5 and col5").grid(row=5, column=5)
# (or)
# myLabel2 = Label(root, text="This is a pgm of row5 and col5")
# myLabel2.grid(row=5, column=5)


from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="This is a pgm of row5 and col5")
# myLabel3 = Label(root, text="This is a pgm of row3 and col3")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=5, column=5)
# myLabel3.grid(row=3, column=3)

root.mainloop()
