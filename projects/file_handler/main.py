filepath = 'example.txt'

def read_Char_by_Char():
    global filepath
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                print(char)


def Number_Of_Lines_And_Word():
    global filepath
    file = open(filepath,'r')


    lines = 0
    words = 0

    for line in file:
        lines += 1
        words += len(line.split())

    
    print("Lines:", lines)
    print("Words:", words)


def Number_of_spaces():
    global filepath
    file = open(filepath,'r')
    spaces = 0
    while True:
        char = file.read(1)
        
        if char == " ":
            spaces += 1
        if not char:
            break
    
    print("Spaces:", spaces)



def findWord(Searchword):
    global filepath
    df = open(filepath)
 
    read = df.read()
    
    df.seek(0)

    arr = []
 
    line = 1
    for word in read:
        if word == '\n':
            line += 1
    
    for i in range(line):
        arr.append(df.readline())

    
    for i in range(len(arr)):
        if Searchword in arr[i]:
            print(f'{Searchword} is present in line ' ,i+1)


read_Char_by_Char()
Number_Of_Lines_And_Word()
Number_of_spaces()
findWord('this')