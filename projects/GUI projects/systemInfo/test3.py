from tkinter import *
from webbrowser import *


lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))


window = Tk()
window.overrideredirect(True)
window.attributes('-topmost', True)
window.geometry("400x400+500+300")
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)
window.mainloop()