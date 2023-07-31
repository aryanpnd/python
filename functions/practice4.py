a = int(input())
b = int(input())

greater = lambda a,b : a if (a>b) else b

print(greater(a,b))