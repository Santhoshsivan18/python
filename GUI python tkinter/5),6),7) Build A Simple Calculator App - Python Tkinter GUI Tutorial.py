# 5),6),7) Build A Simple Calculator App - Python Tkinter GUI Tutorial

from tkinter import *

# Initialize the main window
root = Tk()
root.title("Simple Calculator")  # to change the title of the window
root.configure(bg="#f0f0f0")

# Entry widget for input and output
e = Entry(root, width=35, borderwidth=5, font=("Arial", 14))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e.config(state="readonly")


# Function to handle number button clicks
def button_click(number):
    current = e.get()
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    # e.insert(0, str(e.get()) + str(number)) - this statement causes logic error cause we directly get the input; it erases the previous value and inputs a new value when a new button is pressed.Disclaimer : donot use e.get() directly without assigning a variable to it
    e.config(state="readonly")


# Function to clear the entry widget
def button_clear():
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="readonly")


# Function to perform the calculation
def button_equal():
    try:
        second_num = e.get()
        e.config(state="normal")
        e.delete(0, END)

        if math == "addition":
            e.insert(0, f_num + int(second_num))

        elif math == "subtraction":
            e.insert(0, f_num - int(second_num))

        elif math == "multiplication":
            e.insert(0, f_num * int(second_num))

        elif math == "division":
            if int(second_num) == 0:
                e.insert(0, "Error (div by zero)")
            else:
                e.insert(0, f_num / int(second_num))
        e.config(state="readonly")
    except NameError:
        e.insert(0, "Error")
        e.config(state="readonly")


# Functions to handle different operations
def button_add():
    first_num = e.get()
    global f_num, math
    math = "addition"
    f_num = int(first_num)
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="readonly")


def button_sub():
    first_num = e.get()
    global f_num, math
    math = "subtraction"
    f_num = int(first_num)
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="readonly")


def button_mul():
    first_num = e.get()
    global f_num, math
    math = "multiplication"
    f_num = int(first_num)
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="readonly")


def button_div():
    first_num = e.get()
    global f_num, math
    math = "division"
    f_num = int(first_num)
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="readonly")


# Defining the buttons
# button1 = Button(
#     root, text="1", padx=40, pady=20, borderwidth=5, command=lambda: button_click(1)
# )
# button2 = Button(
#     root, text="2", padx=40, pady=20, borderwidth=5, command=lambda: button_click(2)
# )
# button3 = Button(
#     root, text="3", padx=40, pady=20, borderwidth=5, command=lambda: button_click(3)
# )
# button4 = Button(
#     root, text="4", padx=40, pady=20, borderwidth=5, command=lambda: button_click(4)
# )
# button5 = Button(
#     root, text="5", padx=40, pady=20, borderwidth=5, command=lambda: button_click(5)
# )
# button6 = Button(
#     root, text="6", padx=40, pady=20, borderwidth=5, command=lambda: button_click(6)
# )
# button7 = Button(
#     root, text="7", padx=40, pady=20, borderwidth=5, command=lambda: button_click(7)
# )
# button8 = Button(
#     root, text="8", padx=40, pady=20, borderwidth=5, command=lambda: button_click(8)
# )
# button9 = Button(
#     root, text="9", padx=40, pady=20, borderwidth=5, command=lambda: button_click(9)
# )
# button0 = Button(
#     root, text="0", padx=40, pady=20, borderwidth=5, command=lambda: button_click(0)
# )
# buttonadd = Button(root, text="+", padx=40, pady=20, borderwidth=5, command=button_add)
# buttonsub = Button(root, text="-", padx=40, pady=20, borderwidth=5, command=button_sub)
# buttonmul = Button(root, text="*", padx=40, pady=20, borderwidth=5, command=button_mul)
# buttondiv = Button(root, text="/", padx=40, pady=20, borderwidth=5, command=button_div)
# buttonequal = Button(
#     root, text="=", padx=90, pady=20, borderwidth=5, command=button_equal
# )
# buttonclear = Button(
#     root, text="Clear", padx=82, pady=20, borderwidth=5, command=button_clear
# )

# # displaying the buttons
# button1.grid(row=3, column=0)
# button2.grid(row=3, column=1)
# button3.grid(row=3, column=2)

# button4.grid(row=2, column=0)
# button5.grid(row=2, column=1)
# button6.grid(row=2, column=2)

# button7.grid(row=1, column=0)
# button8.grid(row=1, column=1)
# button9.grid(row=1, column=2)

# button0.grid(row=4, column=0)

# buttonadd.grid(row=5, column=0)
# buttonsub.grid(row=6, column=0)
# buttonmul.grid(row=6, column=1)
# buttondiv.grid(row=6, column=2)

# buttonequal.grid(row=5, column=1, columnspan=2)
# buttonclear.grid(row=4, column=1, columnspan=2)

# root.mainloop()

# Define and place the buttons
button_texts = [
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("0", 4, 0),
]
buttons = []
for text, row, col in button_texts:
    button = Button(
        root,
        text=text,
        padx=40,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=lambda t=text: button_click(t),
        bg="#ffffff",
    )
    button.grid(row=row, column=col)
    buttons.append(button)

    Button(
        root,
        text="+",
        padx=39,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=button_add,
        bg="#ffcccc",
    ).grid(row=5, column=0)
    Button(
        root,
        text="-",
        padx=41,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=button_sub,
        bg="#ffcccc",
    ).grid(row=6, column=0)
    Button(
        root,
        text="*",
        padx=41,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=button_mul,
        bg="#ffcccc",
    ).grid(row=6, column=1)
    Button(
        root,
        text="/",
        padx=41,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=button_div,
        bg="#ffcccc",
    ).grid(row=6, column=2)
    Button(
        root,
        text="=",
        padx=87,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=button_equal,
        bg="#ffcccc",
    ).grid(row=5, column=1, columnspan=2)
    Button(
        root,
        text="Clear",
        padx=79,
        pady=20,
        font=("Arial", 12),
        borderwidth=5,
        command=button_clear,
        bg="#ffcccc",
    ).grid(row=4, column=1, columnspan=2)

root.mainloop()
