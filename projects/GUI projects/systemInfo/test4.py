import psutil

print ('                                                                   ')
print ('----------------------CPU Information summary----------------------')
print ('                                                                   ')

# gives a single float value
vcc=psutil.cpu_count()
print ('Total number of CPUs :',vcc)

vcpu=psutil.cpu_percent()
print ('Total CPUs utilized percentage :',vcpu,'%')

print ('                                                                   ')
print ('----------------------RAM Information summary----------------------')
print ('                                                                   ')
# you can convert that object to a dictionary 
#print(dict(psutil.virtual_memory()._asdict()))
# gives an object with many fields
vvm=psutil.virtual_memory()

x=dict(psutil.virtual_memory()._asdict())

def forloop():
    for i in x:
        print (i,"--",x[i]/1024/1024/1024)#Output will be printed in GBs

forloop()
print ('                                                                   ')
print ('----------------------RAM Utilization summary----------------------')
print ('                                                                   ')
# you can have the percentage of used RAM
print('Percentage of used RAM :',psutil.virtual_memory().percent,'%')
#79.2
# you can calculate percentage of available memory
print('Percentage of available RAM :',psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,'%')
#20.8