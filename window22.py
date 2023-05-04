import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
import os

top = tkinter.Tk()
top.title('Hair Style')
top.config(bg='black')
top.geometry("1366x768")
bgimg = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/bg1.png")

def open_program():
    my_program = filedialog.askopenfilename()
    os.system("%s" % my_program)
    win = tkinter.Toplevel()
    # Define the geometry of the window
    win.geometry("222x305+100+80")

    frame = tkinter.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open(my_program))

    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame, image=img)
    label.pack()
    win.mainloop()


def hss1():
    win = tkinter.Toplevel()
    # Define the geometry of the window
    win.geometry("400x305+800+80")

    frame = tkinter.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("C:/Users/smartuser/PycharmProjects/pythonProject1/photos/sr1.png"))

    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame, image=img)
    label.pack()
    win.mainloop()


def hss2():
    win = tkinter.Toplevel()
    # Define the geometry of the window
    win.geometry("400x305+800+80")

    frame = tkinter.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("C:/Users/smartuser/PycharmProjects/pythonProject1/photos/sr2.png"))

    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame, image=img)
    label.pack()
    win.mainloop()


def hss3():
    win = tkinter.Toplevel()
    # Define the geometry of the window
    win.geometry("400x305+800+80")

    frame = tkinter.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("C:/Users/smartuser/PycharmProjects/pythonProject1/photos/sr3.png"))

    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame, image=img)
    label.pack()
    win.mainloop()


def hss4():
    win = tkinter.Toplevel()
    # Define the geometry of the window
    win.geometry("400x305+800+80")

    frame = tkinter.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("C:/Users/smartuser/PycharmProjects/pythonProject1/photos/sr4.png"))

    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame, image=img)
    label.pack()
    win.mainloop()


bgimg = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/bg1.png")
c5 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/13.png")
c6 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/15.png")
h1 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/hh1.png")
h2 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/hh2.png")
h3 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/hh3.png")
h4 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/hh4.png")

title_label = tkinter.Label(top, text="Hair Style", image=bgimg, font=("Helvetica", 18), bd=5)
title_label.place(anchor='center', x=720, y=412)
upload = tkinter.Button(top, text="Upload", image=c5, command=open_program, cursor='hand2')
upload.place(anchor='nw', width=370, height=100, x=120, y=400)

save = tkinter.Button(top, text="Save", image=c6, cursor='hand2')
save.place(anchor='nw', width=370, height=100, x=813, y=400)

hs1 = tkinter.Button(top, i=h2, command=hss1, cursor='hand2')
hs1.place(anchor='nw', width=120, height=120, x=1064.0, y=530)
hs2 = tkinter.Button(top, i=h3, command=hss2, cursor='hand2')
hs2.place(anchor='nw', width=120, height=120, x=751.0, y=530)
hs3 = tkinter.Button(top, i=h4, command=hss3, cursor='hand2')
hs3.place(anchor='nw', width=120, height=120, x=438.0, y=530)
hs4 = tkinter.Button(top, i=h1, command=hss4, cursor='hand2')
hs4.place(anchor='nw', width=120, height=120, x=125.0, y=530)

top.state('zoomed')
top.mainloop()
