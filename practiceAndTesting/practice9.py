import os

def fileClassifier():
    directoryLists  = os.listdir()
    file = []
    for i in directoryLists:
        if os.path.isfile(i):
            file.append(i)
    print(file)

fileClassifier()
