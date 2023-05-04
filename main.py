import tkinter
import os
from tkinter.ttk import *
from PIL import ImageTk, Image
import cv2

master = tkinter.Tk()
master.title("Hair Design System")
master.config(bg='black')
master.geometry("1366x768")
bgimg = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/bg2.png")
bgimgb1 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/2.png")
bgimgb2 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/1.png")

def hs():

    os.system('python window22.py')

def hc():

    os.system('python window33.py')

title_label = tkinter.Label(master,i=bgimg)
title_label.place(anchor='center', x=650, y=412)

hs = tkinter.Button(master,i=bgimgb1,command=hs, cursor='hand2')
hs.place(anchor='nw', width=387, height=100, x=150, y=380)

hc = tkinter.Button(master,i=bgimgb2,command=hc, cursor='hand2')
hc.place(anchor='nw', width=387, height=100, x=715, y=380)

master.state('zoomed')
master.mainloop()