import psutil
import time

def toGB(bytes):
    return round(((((bytes)/1024/1024))/1024),1) 


systemMemory = psutil.virtual_memory()

totalMemory = round(toGB(systemMemory.total))
memoryUsed = int((toGB(systemMemory.used)))
memoryUsedInPercentage = int((toGB(systemMemory.used)/toGB(systemMemory.total))*100)

while True:
    time.sleep(1)
    print("Total Memory : ",totalMemory,"GB")
    print("Memory Used : ",memoryUsedInPercentage,"%")
    print("Memory Left : ",memoryUsed,"GB from ",totalMemory,"GB")