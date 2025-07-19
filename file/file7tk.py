from tkinter import*

window=tk()
window.title("Lachumi studio")
window.geometry("2048x1024")
l1=Label(window,text="Welcome to Lachumi Studio",fg="Red")
l1.place(x=650,y=100)
l1=Label(window,text="Enter your name",fg="dark blue")
l1.place(x=650,y=200)
e1=Entry(window)
e1.place(x=650,y=250)
l1=Label(window,text="Enter your email",fg="dark blue")
l1.place(x=650,y=300)
e1=Entry(window)
e1.place(x=650,y=350)
l1=Label(window,text="Enter your phone number",fg="dark blue")
l1.place(x=650,y=400)
e1=Entry(window)
e1.place(x=650,y=450)
b1=Button(text="Submit",bg="green",fg="yellow",width=20)
b1.place(x=650,y=500)


import tkinter as tk

window = tk.Tk()
for  i in range(5):
    for  j in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Raw{i}\nColumn{j}")
        label.pack()


window.mainloop()