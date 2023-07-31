if __name__ == '__main__':
    n = int(input())
    list1 = []
    for _ in range(n):
       command = input().split()
       if command[0]!="print":
        if command[0]=="insert":
            list1.insert(int(command[1]),int(command[2]))
        elif command[0]=="remove":
            list1.remove(int(command[1]))
        elif command[0]=="append":
            list1.append(int(command[1]))
        elif command[0]=="sort":
            list1.sort()
        elif command[0]=="pop":
            list1.pop()
        elif command[0]=="reverse":
            list1.reverse()
       if command[0]=="print":
           print(list1)

