# Creating Buttons With TKinter - Python Tkinter GUI Tutorial

from tkinter import *

root = Tk()

# func to make a button do something but until the button is linked to the Button widget using command attribute it doesn't do anything
# No.of button clicks = no.of msgs displayed
def myClick():
    myLabel = Label(root, text="This button is clicked!!").pack()

# command=myClick -> correct , command=myClick() -> incorrect
# fg - foreground/text color , bg - background color -> values should be in quotes but values can be hex codes/color names
myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="pink") #, padx= 50, pady=50) #, state=DISABLED)
myButton.pack()

root.mainloop()