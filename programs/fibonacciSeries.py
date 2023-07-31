a = int(input("enter a number of squence you want to print : "))
n1,n2 = 0,1
b = 0

if a <=0:
    print("please enter a valid number")

else:
    for i in range (0,a):
        print(b)
        n1 = n2
        n2 = b
        b = n1 + n2