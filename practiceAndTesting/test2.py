A, B = input().split()
A, B = [int(A),int(B)]

if A**B > B**A:
    print("first")
elif A**B < B**A:
    print("second")
elif A**B == B**A:
    print("equal")