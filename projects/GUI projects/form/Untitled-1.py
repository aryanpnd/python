from tkinter import *
aryan = Tk()
aryan.title("aryan window")
aryan.geometry('400x400')
aryan.configure(background ="black")

def returnEntry():
    result1 = a1.get()
    result2 = b1.get()
    result3 = c1.get()
    result4 = d1.get()
    print('Name:-',result1)
    print('roll no:',result2)
    print('Class:-',result3)
    print('Marks',result4)

a = Label(aryan, text ="First Name",fg='red',bg='black',font=(50))
a.pack(pady=5)
a1 = Entry(aryan)
a1.pack(padx=10,pady=10)

b = Label(aryan, text ="Roll no",fg='red',bg='black',font=(50))
b.pack()
b1 = Entry(aryan)
b1.pack(padx=10,pady=10)

c = Label(aryan, text ="class",fg='red',bg='black',font=(50))
c.pack()
c1 = Entry(aryan)
c1.pack(padx=10,pady=10)

d = Label(aryan, text ="CS / IP Marks",fg='red',bg='black',font=(50))
d.pack()
d1 = Entry(aryan)
d1.pack(padx=10,pady=10)

btn = Button(aryan, text="Submit",command=returnEntry,bg='lime',font=(50))
btn.pack(padx=10,pady=10)
btn1 = Button(aryan, text="exit",command=aryan.destroy,bg='red',font=(50))
btn1.pack(padx=10,pady=10)


lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + aryan.winfo_x(), event.y - lastClickY + aryan.winfo_y()
    aryan.geometry("+%s+%s" % (x , y))


aryan.overrideredirect(True)
aryan.attributes('-topmost', True)
aryan.bind('<Button-1>', SaveLastClickPos)
aryan.bind('<B1-Motion>', Dragging)

aryan.mainloop()