import tkinter as tk
from tkinter import Frame, ttk
from tkinter.constants import E
import psutil
import time
import platform
from webbrowser import *


tk=tk.Tk()
def toGB(bytes):
        return round(((((bytes)/1024/1024))/1024),1) 


def memoryWindow():
        
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

def cpuWindow():
    
    cpuUsage = psutil.cpu_percent()
    cpuF = psutil.cpu_freq()
    cpuFrequencyCurrent = cpuF.current
    cpuFrequencyminimum = cpuF.min
    cpuFrequencymaximum = cpuF.max

    CpuUsageLabel2.config(text=(cpuUsage,"%"),font='25')
    CpuFrequencyLabel2.config(text=(cpuFrequencyCurrent,"Mhz"),font='25')
    CpuFrequencyMinLabel2.config(text=(cpuFrequencyminimum,"Mhz"),font='25')
    CpuFrequencyMaxLabel2.config(text=(cpuFrequencymaximum,"Mhz"),font='25')

    tk.after(3000,cpuWindow)



def diskWindow():
    
    du = psutil.disk_usage("c:/")
    dc = psutil.disk_io_counters()

    diskTotalSize = round((toGB(du.total)))
    diskUsage = round(toGB(du.used))
    diskfree = round(toGB(du.free))
    diskUsageInPercentage =int(du.percent)
    diskTotalRead = round(toGB(dc.read_bytes))
    diskTotalWrite = round(toGB(dc.write_bytes))

    diskTotalSizeLabel2.config(text=(diskTotalSize,"GB"),font='25')
    diskUsageLabel2.config(text=(diskUsage,"GB"),font='25')
    diskFreeLabel2.config(text=(diskfree,"GB"),font='25')
    diskUsageInPercentageLabel2.config(text=(diskUsageInPercentage,"%"),font="25")
    diskTotalReadLabel2.config(text=(diskTotalRead,"GB"),font="25")
    diskTotalWriteLabel2.config(text=(diskTotalWrite,"GB"),font="25",padding=(0,0,0,30))

    tk.after(1000,cpuWindow)







memoryTitleLable = ttk.Label(tk,text="Memory",font='Times 15',padding=(0,0,0,0))
memoryTitleLable.grid(row=0,column=0)

totalMemoryLabel1 = ttk.Label(tk,text="Total Memory  :  ")
totalMemoryLabel1.grid(row=1,column=0)
totalMemoryLabel2 = ttk.Label(tk)
totalMemoryLabel2.grid(row=1,column=2)


memoryLeftLabel1 = ttk.Label(tk,text="Memory Free  :  ")
memoryLeftLabel1.grid(row=2,column=0)
memoryLeftLabel2 = ttk.Label(tk)
memoryLeftLabel2.grid(row=2,column=2)


memoryUsedInPercentageLabel1 = ttk.Label(tk,text="Memory Used  :  ")
memoryUsedInPercentageLabel1.grid(row=3,column=0)
memoryUsedLabel2 = ttk.Label(tk)
memoryUsedLabel2.grid(row=3,column=2)


memoryUsedInPercentageLabel1 = ttk.Label(tk,text="Memory Used (%)  :  ")
memoryUsedInPercentageLabel1.grid(row=4,column=0)
memoryUsedInPercentageLabel2 = ttk.Label(tk)
memoryUsedInPercentageLabel2.grid(row=4,column=2)






cpuTitleLable = ttk.Label(tk,text="CPU",font='Times 15',padding=(0,30,0,0))
cpuTitleLable.grid(row=6,column=0)

CpuLabel1 = ttk.Label(tk,text="CPU  :  :",padding=(0,0,0,0))
CpuLabel1.grid(row=7,column=0)
CpuLabel2 = ttk.Label(tk,text = platform.processor(),wraplength=150)
CpuLabel2.grid(row=7,column=2)

totalCpuLabel1 = ttk.Label(tk,text="Total CPU  :  ")
totalCpuLabel1.grid(row=8,column=0)
totalCpuLabel2 = ttk.Label(tk,text=psutil.cpu_count(),font='25')
totalCpuLabel2.grid(row=8,column=2)

CpuUsageLabel1 = ttk.Label(tk,text="CPU Usage :  ")
CpuUsageLabel1.grid(row=9,column=0)
CpuUsageLabel2 = ttk.Label(tk)
CpuUsageLabel2.grid(row=9,column=2)

CpuFrequencyLabel1 = ttk.Label(tk,text="CPU Frequency :  ")
CpuFrequencyLabel1.grid(row=10,column=0)
CpuFrequencyLabel2 = ttk.Label(tk)
CpuFrequencyLabel2.grid(row=10,column=2)

CpuFrequencyMinLabel1 = ttk.Label(tk,text="CPU Frequency (min) :  ")
CpuFrequencyMinLabel1.grid(row=11,column=0)
CpuFrequencyMinLabel2 = ttk.Label(tk)
CpuFrequencyMinLabel2.grid(row=11,column=2)

CpuFrequencyMaxLabel1 = ttk.Label(tk,text="CPU Frequency (max) :  ")
CpuFrequencyMaxLabel1.grid(row=12,column=0)
CpuFrequencyMaxLabel2 = ttk.Label(tk)
CpuFrequencyMaxLabel2.grid(row=12,column=2)






diskTitleLable = ttk.Label(tk,text="Disk",font='Times 15',padding=(40,10,10,15))
diskTitleLable.grid(row=0,column=4)

diskTotalSizeLabel1 = ttk.Label(tk,text="Total Size (c:/)   :  ",padding=(0,0,0,0))
diskTotalSizeLabel1.grid(row=1,column=4)
diskTotalSizeLabel2 = ttk.Label(tk)
diskTotalSizeLabel2.grid(row=1,column=6)

diskUsageLabel1 = ttk.Label(tk,text="Used   :  ",padding=(0,0,0,0))
diskUsageLabel1.grid(row=2,column=4)
diskUsageLabel2 = ttk.Label(tk)
diskUsageLabel2.grid(row=2,column=6)

diskFreeLabel1 = ttk.Label(tk,text="Free   :  ",padding=(0,0,0,0))
diskFreeLabel1.grid(row=3,column=4)
diskFreeLabel2 = ttk.Label(tk)
diskFreeLabel2.grid(row=3,column=6)

diskUsageInPercentageLabel1 = ttk.Label(tk,text="Used (%)   :  ",padding=(0,0,0,0))
diskUsageInPercentageLabel1.grid(row=4,column=4)
diskUsageInPercentageLabel2 = ttk.Label(tk)
diskUsageInPercentageLabel2.grid(row=4,column=6)

diskTotalReadLabel1 = ttk.Label(tk,text="Total Read   :  ",padding=(0,0,0,0))
diskTotalReadLabel1.grid(row=5,column=4)
diskTotalReadLabel2 = ttk.Label(tk)
diskTotalReadLabel2.grid(row=5,column=6)

diskTotalWriteLabel1 = ttk.Label(tk,text="Total Write   :  ",padding=(0,0,0,30))
diskTotalWriteLabel1.grid(row=6,column=4)
diskTotalWriteLabel2 = ttk.Label(tk)
diskTotalWriteLabel2.grid(row=6,column=6)


exitButton = ttk.Button(tk,text='Exit',command=lambda:tk.destroy())
exitButton.grid(row=21,column=4)



memoryWindow()
cpuWindow()
diskWindow()


lastClickX = 0
lastClickY = 0


# def SaveLastClickPos(event):
#     global lastClickX, lastClickY
#     lastClickX = event.x
#     lastClickY = event.y


# def Dragging(event):
#     x, y = event.x - lastClickX + tk.winfo_x(), event.y - lastClickY + tk.winfo_y()
#     tk.geometry("+%s+%s" % (x , y))


tk.geometry("300x300")
tk.minsize(height=400,width=450)
tk.minsize(height=400,width=450)
# tk.overrideredirect(True)
# tk.attributes('-topmost', True)
tk.geometry("400x400+500+300")
# tk.bind('<Button-1>', SaveLastClickPos)
# tk.bind('<B1-Motion>', Dragging)

tk.mainloop()