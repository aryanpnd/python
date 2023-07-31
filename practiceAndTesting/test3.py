n = int(input())

a = []
for i in range (n):
    A, B, C = input().split()
    A, B, C = [int(A),int(B),int(C)]
    

    if ((A and C)-B)==0 or ((B and C)-A)==0 or ((A and B)-C)==0:
        a.append("Yes")     
    else: b = a.append("No")

for i in a:
    print(i)
