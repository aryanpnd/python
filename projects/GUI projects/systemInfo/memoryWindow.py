import tkinter as tk
from tkinter import ttk
import psutil

def memoryWindow():

    def toGB(bytes):
        return round(((((bytes)/1024/1024))/1024),1) 

        
    systemMemory = psutil.virtual_memory()


    totalMemory = round(toGB(systemMemory.total))
    memoryLeft = int(totalMemory-(toGB(systemMemory.used)))
    memoryUsed = int(toGB(systemMemory.used))
    memoryUsedInPercentage = int((toGB(systemMemory.used)/toGB(systemMemory.total))*100)


    totalMemoryLabel2.config(text=(totalMemory,"GB"),font='25')
    memoryLeftLabel2.config(text=(memoryLeft,"GB"),font='25')
    memoryUsedLabel2.config(text=(memoryUsed,"GB"),font='25')
    memoryUsedInPercentageLabel2.config(text=(memoryUsedInPercentage,"%"),font='25')


    tk.after(1000,memoryWindow)



memoryFrame = ttk.Frame(tk,padding=(10,10,10,10))

memoryTitleLable = ttk.Label(memoryFrame,text="Memory",font='Times 15',padding=(0,0,0,10))
memoryTitleLable.grid(row=0,column=0)

totalMemoryLabel1 = ttk.Label(memoryFrame,text="Total Memory  :  ")
totalMemoryLabel1.grid(row=1,column=0)
totalMemoryLabel2 = ttk.Label(memoryFrame)
totalMemoryLabel2.grid(row=1,column=2)


memoryLeftLabel1 = ttk.Label(memoryFrame,text="Memory Free  :  ")
memoryLeftLabel1.grid(row=2,column=0)
memoryLeftLabel2 = ttk.Label(memoryFrame)
memoryLeftLabel2.grid(row=2,column=2)


memoryUsedInPercentageLabel1 = ttk.Label(memoryFrame,text="Memory Used  :  ")
memoryUsedInPercentageLabel1.grid(row=3,column=0)
memoryUsedLabel2 = ttk.Label(memoryFrame)
memoryUsedLabel2.grid(row=3,column=2)


memoryUsedInPercentageLabel1 = ttk.Label(memoryFrame,text="Memory Used (%)  :  ")
memoryUsedInPercentageLabel1.grid(row=4,column=0)
memoryUsedInPercentageLabel2 = ttk.Label(memoryFrame)
memoryUsedInPercentageLabel2.grid(row=4,column=2)


memoryFrame.grid(row=1,column=1)

memoryWindow()