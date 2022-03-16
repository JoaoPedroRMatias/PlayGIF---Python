from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

def playGif():
    while True:
        global img
        img = Image.open('kirby.gif')

        lbl = Label(root)
        lbl.place(x=0, y=20)

        for img in ImageSequence.Iterator(img):
            img = ImageTk.PhotoImage(img)
            lbl.config(image = img)
            time.sleep(0.09)
            root.update()
