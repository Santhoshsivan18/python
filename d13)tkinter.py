import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")
"""
# Label
label = tk.Label(root, text="Name", bg="black", fg="red").pack()
entry = tk.Entry(root).pack()
"""
"""
# Listbox section
tk.Label(root, text="Listbox Example:").pack()
listbox = tk.Listbox(root)
listbox.insert(1, "python")
listbox.insert(2, "java")
listbox.insert(3, "C")
listbox.pack()
"""
"""
# Messagebox section
msg = "This is a msg"
message = Message(root, text=msg, font=("Ariel", 20), fg="red", width=600)
message.config(bg="black")
# root.config(bg="green")
message.pack()

messagebox.showerror("Error", "Invalid credentials")
messagebox.showwarning("Warning", "There's not enough space")
messagebox.showinfo("Information", "Succesfully installed")


def quit():
    a = messagebox.askyesno("Warning", "Do you want to quit?")
    if a:
        root.destroy()
    else:
        root.mainloop()


b = Button(root, text="Quit", command=quit).pack(side=RIGHT)
"""
"""
# Scale section - default orient is vertical
w = Scale(root, from_=0, to=400)
w.pack()
w = Scale(root, from_=0, to=400, orient=HORIZONTAL)
# w = Scale(root, from_=0, to=400, orient='horizontal')
w.pack()
"""
"""
# Text section - like paragraph
t = Text(root, height=25, width=30)
t.insert(END, "python")
# t.insert('end',"python")
t.pack()
"""
"""
# Toplevel section
def new():
    top = Toplevel(root)
    top.title("Python")
    print("hello")

b = Button(root, text="new window", command=new, bd=5)
b.place(x=50, y=50)
"""
"""
# Spinbox section
w=Spinbox(root,font=("bold",30), from_=-89,to=100).pack()
"""
"""
# Pannedwindow section - can be combined with root/tk
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=TRUE)

left = Text(m1, bd=15)

# bt = Button(m1, text="click", command=num)
# m1.add(bt)
m1.add(left)

m2 = PanedWindow(m1, orient=HORIZONTAL)

m1.add(m2)

top = Scale(m2, bd=5, orient=HORIZONTAL)
m2.add(top)
"""
"""
# Scrollbar section - set & yview are inbuilt funcs
root.geometry("600x600")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
li = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    li.insert(END, "This is line number: " + str(line))
li.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=li.yview)
"""
"""
# Canvas section - x1, y1, x2, y2
c = Canvas(root, bg="light blue", height=250, width=300)
line = c.create_line(80, 30, 160, 150, fill="black")
rect = c.create_rectangle(80, 30, 160, 150, fill="green")
oval = c.create_oval(80, 30, 160, 150, fill="red")
c.pack()
"""
"""
# Entry box
# 400px wide 250px height
# element placing system - pack(),grid(),place()
root.geometry("400x250")

n = StringVar()
e = StringVar()
p = StringVar()

name = Label(root, text="Name", font=("times", 25), fg="red").grid(row=0, column=0)
email = Label(root, text="Email", font=("arial", 25), fg="green").grid(row=1, column=0)
password = Label(root, text="Password", font=("calibre", 25), fg="blue").place(
    x=0, y=110
)


def submit():
    name = n.get()
    email = e.get()
    password = p.get()

    print("The name is ", name)
    print("The email is ", email)
    print("The password is ", password)

    n.set("")
    e.set("")
    p.set("")


e1 = Entry(root, textvariable=n).place(x=150, y=20)  # .grid(row=0,column=1)
e2 = Entry(root, textvariable=e).place(x=150, y=60)  # .grid(row=1,column=1)
e3 = Entry(root, show="*", textvariable=p).place(x=150, y=120)
b1 = Button(
    root,
    text="Submit",
    activebackground="pink",
    fg="red",
    activeforeground="blue",
    command=submit,
).place(x=150, y=170)
b2 = Button(root, text="Cancel", command=root.destroy).place(x=250, y=170)
"""
"""
# Menu section
def show_about():
    messagebox.showinfo("About", "Tkinter Example Application")
    print("Hi...")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=1)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
"""
# File Dialogue
root.resizable(False, False)
root.geometry("300x300")


def select_file():
    filetypes = (("Text files", "*.txt"), ("PDF files", "*.pdf"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="/", filetypes=filetypes
    )
    
    messagebox.showinfo(title="Selected file", message=filename)

b1 = Button(root,text="Open a file",command=select_file).pack()
b2 = Button(root,text="Cancel",command=root.destroy).pack()

# Run the application
root.mainloop()
