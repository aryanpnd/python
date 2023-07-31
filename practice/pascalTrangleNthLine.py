# Pascal's Triangle
# Description
# Pascal's triangle is a very interesting mathematical concept.

# The following is an 8-level Pascal's triangle. Each number here is a sum of the two numbers directly above it:





# You can read about Pascal's triangle here.

# Your task is to print an nth level of Pascal's triangle.

# The input will contain an integer n.

# The output will contain 1 line of the list of numbers representing the nth row of Pascal's triangle.



# Sample Input:

# 6

# Sample Output:



# [1, 5, 10, 10, 5, 1]
# Execution Time Limit
# 10 seconds

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line
 
n=int(input())
print(pascal(n))