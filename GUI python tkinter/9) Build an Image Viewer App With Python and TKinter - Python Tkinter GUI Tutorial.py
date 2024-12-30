# 9) Build an Image Viewer App With Python and TKinter - Python Tkinter GUI Tutorial


from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Photo view app")

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


# label = Label(root, text="").grid()
Image_list = [img1, img2, img3, img4, img5, img6, img7, img8]

# for i in Image_list:
my_label = Label(root, image=img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_num):
    global my_label, button_forward, button_back

    my_label.grid_forget()
    my_label = Label(root, image=Image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    if img_num == len(Image_list) - 1:
        button_forward.config(state="disabled")
    else:
        button_forward.config(state="normal", command=lambda: forward(img_num + 1))

    button_back.config(state="normal", command=lambda: back(img_num - 1))
    # button_back.grid(row=1, column=0)


def back(img_num):
    global my_label, button_forward, button_back

    my_label.grid_forget()
    my_label = Label(root, image=Image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    if img_num == 0:
        button_back.config(state="disabled")
    else:
        button_back.config(state="normal", command=lambda: back(img_num - 1))

    button_forward.config(state="normal", command=lambda: forward(img_num + 1))


button_back = Button(root, text="<<", command=lambda: back(0), state="disabled")
button_back.grid(row=1, column=0)
button_exit = Button(root, text="Exit App", command=root.quit)
button_exit.grid(row=1, column=1)
button_forward = Button(root, text=">>", command=lambda: forward(1))
button_forward.grid(row=1, column=2)

root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk

# class ImageViewer:
#     def __init__(s, root):
#         s.root = root
#         s.root.title("Photo View App")
        
#         # List of image paths
#         s.image_paths = [
#             r"GUI python tkinter\pics\cat-8762411_1280.png",
#             r"GUI python tkinter\pics\flower_crocus-1279508_640.png",
#             r"GUI python tkinter\pics\mustang_car-967387_640.png",
#             r"GUI python tkinter\pics\owl-2569202_640.png",
#             r"GUI python tkinter\pics\paper.png",
#             r"GUI python tkinter\pics\pyramid.ico",
#             r"GUI python tkinter\pics\rock.png",
#             r"GUI python tkinter\pics\scissors.png"
#         ]
        
#         # Load images
#         s.images = [ImageTk.PhotoImage(Image.open(path).resize((300, 300), Image.LANCZOS)) for path in s.image_paths]
        
#         # Current image index
#         s.current_image_idx = 0

#         # Label to display the image
#         s.my_label = Label(root, image=s.images[s.current_image_idx])
#         s.my_label.grid(row=0, column=0, columnspan=3)

#         # Label to display the image name
#         s.name_label = Label(root, text=s.get_image_name())
#         s.name_label.grid(row=1, column=0, columnspan=3)
        
#         # Status bar to display the image index in the middle
#         s.status = Label(root, text=f"Image 1 of {len(s.images)}", bd=1, relief=SUNKEN, anchor=CENTER)
#         s.status.grid(row=2, column=0, columnspan=3, pady=10)  # Added padding for spacing

#         # Buttons for navigation
#         s.button_back = Button(root, text="<<", command=s.back, state=DISABLED)
#         s.button_back.grid(row=3, column=0)
#         s.button_exit = Button(root, text="Exit App", command=root.quit)
#         s.button_exit.grid(row=3, column=1)
#         s.button_forward = Button(root, text=">>", command=s.forward)
#         s.button_forward.grid(row=3, column=2)

#     def forward(s):
#         s.current_image_idx += 1
#         s.my_label.config(image=s.images[s.current_image_idx])
#         s.name_label.config(text=s.get_image_name())
#         s.update_buttons()
#         s.update_status()

#     def back(s):
#         s.current_image_idx -= 1
#         s.my_label.config(image=s.images[s.current_image_idx])
#         s.name_label.config(text=s.get_image_name())
#         s.update_buttons()
#         s.update_status()

#     def get_image_name(s):
#         return s.image_paths[s.current_image_idx].split("\\")[-1]

#     def update_buttons(s):
#         if s.current_image_idx == 0:
#             s.button_back.config(state=DISABLED)
#         else:
#             s.button_back.config(state=NORMAL)

#         if s.current_image_idx == len(s.images) - 1:
#             s.button_forward.config(state=DISABLED)
#         else:
#             s.button_forward.config(state=NORMAL)

#     def update_status(s):
#         s.status.config(text=f"Image {s.current_image_idx + 1} of {len(s.images)}")

# def main():
#     root = Tk()
#     app = ImageViewer(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
