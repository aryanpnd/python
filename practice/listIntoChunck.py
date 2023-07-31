# Break the List
# Description
# Write a Python program to divide a given list into chunks of size k.



# The number of elements in the list need not be divisible by k.



# For example, if you want to divide the list [1,2,3,4,5,6,7] into chunk size k=4, then the first chunk will be [1,2,3,4], and the second one will have [5,6,7], i.e. the last chunk need not have k elements.



# The input will have two lines, the first line would have the list, and the second line would have the value of k(the code for taking input has already been written, you should not change that).



# The final output should have the list chunks in different lines.



# Sample Input:

# [1,2,3,4,5,6,7,8,9]

# 3

# Sample Output:



# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

import ast

input_str = input()
input_list = ast.literal_eval(input_str)

lis=input_list[0]
k=input_list[1]

for i in range(0, len(lis), k):  
    print(lis[i: i + k]) 