# from tkinter import *
# from pillow import Image, ImageTk

# root = Tk()
# root.title('img')
# root.geometry('400x400')

# uplode = Image.open('img.png')


from tkinter import *

from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well

root = Tk()

root.title('image')

root.geometry('400x400')

# Now use Image.open to open and identify the given image file.

upload = Image.open("img.png")

# Convert this Image to Tkinter compatible image

image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label

label = Label(root, image=image, height=350, width=300)

label.place(x=50, y=0)

label2 = Label(root, text="This is how you add image in Tkinter Window")

label2.place(x=40, y=360)

# Run the application

root.mainloop()