# Yt vid link : https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# 1) Create Graphical User Interfaces With Python And TKinter
# Everything in tkinter is a widget
# Everything in tkinter takes place in 2 steps : define a thing and put it up on the screen

from tkinter import *

# main window
root = Tk()
# Creating a label widget
myLabel = Label(root, text="Hello World!")
# Putting it in the screen
myLabel.pack()

# this following line loops the main root code monitoring the cursors movements and it ends when the user closes the o/p window using the red x button.
root.mainloop()
