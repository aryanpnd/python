n = int(input("Enter a number : "))
b = 0

for i in range (1,n):
    if (n%i==0):
        b = b + i
if b == n:
    print(f"{n} is a perfect number")

else:
    print(f"{n} is not a perfect number")