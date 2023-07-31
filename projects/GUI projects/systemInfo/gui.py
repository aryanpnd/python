import threading
from tkinter import * 
from tkinter import ttk
# import systemInfo as si
import psutil
import time
from threading import *


# creating root
root = Tk()


def mainWindow():
    def toGB(bytes):
        return round(((((bytes)/1024/1024))/1024),1) 


    systemMemory = psutil.virtual_memory()


    time.sleep(1)
    while True:
        totalMemory = round(toGB(systemMemory.total))
        memoryUsed = int((toGB(systemMemory.used)))
        memoryUsedInPercentage = int((toGB(systemMemory.used)/toGB(systemMemory.total))*100)

    print(memoryUsed)    
    

a = ttk.Label(root, text="").pack()
b = ttk.Button(root,command=mainWindow).pack()

threading.Thread(target=mainWindow).start()
  
root.mainloop()


#                                  NOT POSSIBLE DUE TO THREADING