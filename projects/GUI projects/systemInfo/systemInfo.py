import psutil
import time
import platform

def toGB(bytes):
    return round(((((bytes)/1024/1024))/1024),1) 


systemMemory = psutil.virtual_memory()
print(systemMemory)
print(platform.processor())

totalMemory = round(toGB(systemMemory.total))
memoryUsed = int(totalMemory-(toGB(systemMemory.used)))
memoryUsedInPercentage = int((toGB(systemMemory.used)/toGB(systemMemory.total))*100)
cpu = psutil.cpu_freq()
du = psutil.disk_usage('/')
du2 = psutil.disk_io_counters()
while True:
    time.sleep(1)
    print("Total Memory : ",totalMemory,"GB")
    print("Memory Used : ",memoryUsedInPercentage,"%")
    print("Memory Left : ",memoryUsed,"GB from ",totalMemory,"GB")\

    print(psutil.cpu_percent())
    print(cpu.current)
    print(cpu.min)
    print(cpu.max)
    print(round(toGB(du.total)))
    print(round(toGB(du2.read_bytes)))