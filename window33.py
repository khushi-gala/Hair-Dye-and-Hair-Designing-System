import tkinter
from tkinter import filedialog, Button
import cv2
import os
import numpy as np
from PIL import Image, ImageTk

def open_program():
    my_program = filedialog.askopenfilename()
    os.system("%s" % my_program)
    win = tkinter.Toplevel()
    # Define the geometry of the window
    win.geometry("200x200+800+100")

    frame = tkinter.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open(my_program))

    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame, image=img)
    label.pack()
    win.mainloop()

def save():
    pass

def blue():
    # Load input image
    img = cv2.imread('C:/Users/smartuser/PycharmProjects/pythonProject1/photos/womenn.jpg')

    # Apply hair segmentation using a pre-trained model or algorithm
    # Here's an example using OpenCV's CascadeClassifier
    haar_cascade = cv2.CascadeClassifier(
        r'C:\Users\smartuser\AppData\Roaming\Python\Python311\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=3.1, minNeighbors=2)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:2 + y + 2 * h, x:2 + x + 2 * w]
        roi_color = img[y:2 + y + 2 * h, x:2 + x + 2 * w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 0)

    # Apply desired hair color or design to the hair region of the image
    # Here's an example of applying a blue hair dye to the hair region
    mask = np.zeros(img.shape[0:2], np.uint8)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + 2 * h, x:x + 2 * w]
        roi_color = img[y:y + h, x:x + w]
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    blue_hair = np.zeros_like(img)
    blue_hair[:, :, 0] = 255  # Set blue channel to 255
    blue_hair = cv2.bitwise_and(blue_hair, blue_hair, mask=mask)
    hair = cv2.addWeighted(blue_hair, 1.5, img, 1.5, 2)

    # Blend modified hair region with original image
    result = cv2.addWeighted(hair, 0.5, img, 0.5, 3)

    # Display result
    cv2.imshow('Result', result)
    cv2.imwrite('C:/Users/smartuser/PycharmProjects/pythonProject1/Output/blue.png', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def red():
    # Load input image
    img = cv2.imread('C:/Users/smartuser/PycharmProjects/pythonProject1/photos/womenn.jpg')

    # Apply hair segmentation using a pre-trained model or algorithm
    # Here's an example using OpenCV's CascadeClassifier
    haar_cascade = cv2.CascadeClassifier(
        r'C:\Users\smartuser\AppData\Roaming\Python\Python311\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=3.1, minNeighbors=2)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:2 + y + 2 * h, x:2 + x + 2 * w]
        roi_color = img[y:2 + y + 2 * h, x:2 + x + 2 * w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 2, 255), 0)

    # Apply desired hair color or design to the hair region of the image
    # Here's an example of applying a red hair dye to the hair region
    mask = np.zeros(img.shape[:2], dtype='uint8')
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    red_hair = np.zeros_like(img)
    red_hair[:, :, 0] = 0  # Set blue channel to 255
    red_hair[:, :, 1] = 0
    red_hair[:, :, 2] = 255
    red_hair = cv2.bitwise_and(red_hair, red_hair, mask=mask)
    hair = cv2.addWeighted(red_hair, 1, img, 1.1, 5)

    # Blend modified hair region with original image
    result = cv2.addWeighted(hair, 0.3, img, 1.0, 3)

    # Display result
    cv2.imshow('Result', result)
    cv2.imwrite('C:/Users/smartuser/PycharmProjects/pythonProject1/Output/red.png', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pink():
    # Load input image
    img = cv2.imread('C:/Users/smartuser/PycharmProjects/pythonProject1/photos/womenn.jpg')

    # Apply hair segmentation using a pre-trained model or algorithm
    # Here's an example using OpenCV's CascadeClassifier
    haar_cascade = cv2.CascadeClassifier(
        r'C:\Users\smartuser\AppData\Roaming\Python\Python311\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=3.1, minNeighbors=1)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:2 + y + 2 * h, x:2 + x + 2 * w]
        roi_color = img[y:2 + y + 2 * h, x:2 + x + 2 * w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 2), 0)

    # Apply desired hair color or design to the hair region of the image
    # Here's an example of applying a pink hair dye to the hair region
    mask = np.zeros(img.shape[:2], dtype='uint8')
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    pink_hair = np.zeros_like(img)
    pink_hair[:, :, 0] = 10  # Set blue channel to 255
    pink_hair[:, :, 1] = 0
    pink_hair[:, :, 2] = 250
    pink_hair = cv2.bitwise_and(pink_hair, pink_hair, mask=mask)
    hair = cv2.addWeighted(pink_hair, 10, img, 1.1, 5)

    # Blend modified hair region with original image
    result = cv2.addWeighted(hair, 0.5, img, 0.6, 6)

    # Display result
    cv2.imshow('Result', result)
    cv2.imwrite('C:/Users/smartuser/PycharmProjects/pythonProject1/Output/pink.png', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blonde():
    # Load input image
    img = cv2.imread('C:/Users/smartuser/PycharmProjects/pythonProject1/photos/womenn.jpg')

    # Apply hair segmentation using a pre-trained model or algorithm
    # Here's an example using OpenCV's CascadeClassifier
    haar_cascade = cv2.CascadeClassifier(
        r'C:\Users\smartuser\AppData\Roaming\Python\Python311\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=3.1, minNeighbors=2)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:2 + y + 2 * h, x:2 + x + 2 * w]
        roi_color = img[y:2 + y + 2 * h, x:2 + x + 2 * w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (3, 255, 255), 0)

    # Apply desired hair color or design to the hair region of the image
    # Here's an example of applying a blonde hair dye to the hair region
    mask = np.zeros(img.shape[:2], np.uint8)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    blonde_hair = np.zeros_like(img)
    blonde_hair[:, :, 0] = 3  # Set blue channel to 255
    blonde_hair[:, :, 1] = 250
    blonde_hair[:, :, 2] = 255
    blonde_hair = cv2.bitwise_and(blonde_hair, blonde_hair, mask=mask)
    hair = cv2.addWeighted(blonde_hair, 1, img, 1, 2)

    # Blend modified hair region with original image
    result = cv2.addWeighted(hair, 0.2, img, 1, 3)

    # Display result
    cv2.imshow('Result', result)
    cv2.imwrite('C:/Users/smartuser/PycharmProjects/pythonProject1/Output/blonde.png', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


top2 = tkinter.Tk()
bgimg = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/bg1.png")
c1 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/9.png")
c2 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/10.png")
c3 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/11.png")
c4 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/8.png")
c5 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/13.png")
c6 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/15.png")
c7 = tkinter.PhotoImage(file="C:/Users/smartuser/PycharmProjects/pythonProject1/photos/12.png")

top2.title('Hair Color')
top2.config(bg='black')
top2.geometry("1366x768")

title_label = tkinter.Label(top2, text="Hair Color", image=bgimg, font=("Helvetica", 18), bd=5)
title_label.place(anchor='center', x=720, y=412)
upload = tkinter.Button(top2, i=c5, text="Upload", command=open_program, cursor='hand2')
upload.place(anchor='nw', width=370, height=100, x=80, y=400)
save = tkinter.Button(top2, i=c6, text="Save", cursor='hand2')
save.place(anchor='nw', width=370, height=100, x=827, y=400)

Red = tkinter.Button(top2, i=c3, text="Red", command=red, cursor='hand2')
Red.place(anchor='nw', width=220, height=100, x=80.0, y=530)
Blonde = tkinter.Button(top2, i=c7, text="Brown", command=blonde, cursor='hand2')
Blonde.place(anchor='nw', width=220, height=100, x=380.0, y=530)
Pink = tkinter.Button(top2, i=c1, text="Pink", command=pink, cursor='hand2')
Pink.place(anchor='nw', width=220, height=100, x=680.0, y=530)
Blue = tkinter.Button(top2, i=c4, text="Blue", command=blue, cursor='hand2')
Blue.place(anchor='nw', width=220, height=100, x=980.0, y=530)
top2.state('zoomed')
top2.mainloop()