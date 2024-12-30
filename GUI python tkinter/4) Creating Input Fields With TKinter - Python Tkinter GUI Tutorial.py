# 4) Creating Input Fields With TKinter - Python Tkinter GUI Tutorial

from tkinter import *

root = Tk()
# Entry widget to get input from user and get() method to process that data
e = Entry(root, width=50, borderwidth=15)  # , fg="green", bg="black")
e.pack()
# insert() method inserts a default value in the entry box widget.
# It's similar to to a placeholder value but not exactly since we have to delete the text to input a new value
e.insert(0, "Your Name")


def myClick():
    hello = "Hello " + e.get()
    # use + operator(concatenation) and not , operator to print multiple values
    # myLabel = Label(root, text=e.get()+" clicked this button").pack()
    myLabel = Label(root, text=hello).pack()
    # myLabel = Label(root, text=e.get()).pack()


myButton = Button(root, text="Enter Name", command=myClick)
myButton.pack()

root.mainloop()
