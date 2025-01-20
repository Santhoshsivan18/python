# 10) Adding A Status Bar - Python Tkinter GUI Tutorial


from tkinter import *
from PIL import Image, ImageTk

# Initialize the main application window
root = Tk()
root.title("Photo view app")

# Load and resize images
img1 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\cat-8762411_1280.png").resize(
        (300, 300), Image.LANCZOS
    )
)
img2 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\flower_crocus-1279508_640.png").resize(
        (300, 300), Image.LANCZOS
    )
)
img3 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\mustang_car-967387_640.png").resize(
        (300, 300), Image.LANCZOS
    )
)
img4 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\owl-2569202_640.png").resize(
        (300, 300), Image.LANCZOS
    )
)
img5 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\paper.png").resize((300, 300), Image.LANCZOS)
)
img6 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\pyramid.ico").resize((300, 300), Image.LANCZOS)
)
img7 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\rock.png").resize((300, 300), Image.LANCZOS)
)
img8 = ImageTk.PhotoImage(
    Image.open(r"GUI python tkinter\pics\scissors.png").resize(
        (300, 300), Image.LANCZOS
    )
)

# Store images in a list
Image_list = [img1, img2, img3, img4, img5, img6, img7, img8]

# Create and display the initial status bar
status = Label(root, text="Image 1 of " + str(len(Image_list)), bd=5, relief=SUNKEN)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# Display the first image
my_label = Label(root, image=img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_num):
    """Move to the next image."""
    global my_label, button_forward, button_back

    # Remove the previous image
    my_label.grid_forget()

    # Display the new image
    my_label = Label(root, image=Image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    # Disable forward button if it's the last image
    if img_num == len(Image_list) - 1:
        button_forward.config(state="disabled")
    else:
        button_forward.config(state="normal", command=lambda: forward(img_num + 1))

    # Enable back button
    button_back.config(state="normal", command=lambda: back(img_num - 1))

    # Update status bar
    status.config(text="Image " + str(img_num + 1) + " of " + str(len(Image_list)))


def back(img_num):
    """Move to the previous image."""
    global my_label, button_forward, button_back

    # Remove the previous image
    my_label.grid_forget()

    # Display the new image
    my_label = Label(root, image=Image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    # Disable back button if it's the first image
    if img_num == 0:
        button_back.config(state="disabled")
    else:
        button_back.config(state="normal", command=lambda: back(img_num - 1))

    # Enable forward button
    button_forward.config(state="normal", command=lambda: forward(img_num + 1))

    # Update status bar
    status.config(text="Image " + str(img_num + 1) + " of " + str(len(Image_list)))


# Create navigation buttons
button_back = Button(root, text="<<", command=lambda: back(0), state="disabled")
button_back.grid(row=1, column=0)
button_exit = Button(root, text="Exit App", command=root.quit)
button_exit.grid(row=1, column=1)
button_forward = Button(root, text=">>", command=lambda: forward(1))
button_forward.grid(row=1, column=2, pady=10)

root.mainloop()
