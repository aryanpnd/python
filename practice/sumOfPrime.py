# Sum of Primes
# Description
# Write a Python code to find the sum of prime numbers from 2 to 'n', where 'n' is a positive integer entered by the user.



# Note: n can be non-prime or prime. You have to find the sum of primes till 'n' and not the sum of 'n' prime numbers. i.e., for input 10, the output should be 17.



# Hint: You can try using lambda functions and comprehensions to reduce the lines of code you have to write.



# Input: A positive integer n.

# Output: A integer denoting the sum of primes less than or equal to n



# Sample Input:

# 5

# Sample Output:

# 10

# Execution Time Limit
# 15 seconds

n = int(input())
a = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
           break
    else:
        a = a + i
print(a)