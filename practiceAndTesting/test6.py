for _ in range(int(input())):
    l=list(map(int,input().split()))
    l.sort()
    while(l[-1]>0 and l[-2]>0):
        l[-1]-=1
        l[-2]-=1
        l.sort()
    
    if(l[-1]!=0 or l[-2]!=0):
        print("No")
    else:
        print("Yes")