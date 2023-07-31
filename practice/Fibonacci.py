# Fibonacci Series
# Description
# Compute and display Fibonacci series up to 'n' terms where 'n' is a positive integer entered by the user.

# You can go here to read about the Fibonacci series.

# Sample Input:

# 5

# Sample Output:

# 0

# 1

# 1

# 2

# 3

# Execution Time Limit
# 10 seconds

a = int(input())
n1,n2 = 0,1
b = 0

if a <=0:
    print()

else:
    for i in range (0,a):
        print(b)
        n1 = n2
        n2 = b
        b = n1 + n2