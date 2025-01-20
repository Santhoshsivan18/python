# 13) Message Boxes with TKinter - Python Tkinter GUI Tutorial

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title("Message box")


def popup():
    # response = messagebox.showinfo("Info popup", "hello world")
    # response = messagebox.showwarning("Warning popup", "hello world")
    # response = messagebox.showerror("Error popup", "hello world")
    # response = messagebox.askyesno("Askyesno popup", "hello world")
    response = messagebox.askquestion("Askquestion popup", "hello world")
    # response = messagebox.askokcancel("Askokcancel popup", "hello world")
    Label(root, text=response).pack()
    if response == "yes": #askquestion
    # if response == True: #askyesno
    # if response == 1: #askyesno
        label1 = Label(root, text="You clicked yes!!", bg="green").pack()
    elif response == "no": #askquestion
    # elif response == False: #askyesno
    # elif response == 0: #askyesno
        label2 = Label(root, text="You clicked no!!", bg="red").pack()


button = Button(root, text="Popup", command=popup).pack()

root.mainloop()
