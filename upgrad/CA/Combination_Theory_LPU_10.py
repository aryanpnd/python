# Combination Theory LPU 10
# Description
# You are given a list of n natural numbers. You select m numbers from the list at random. 
# Find the probability that at least one of the selected alphabets is "x" where x is a number given to you as input.
# The first line of input will contain a list of numbers. The second line will contain m and the third line will contain x.
# The output should be printed out as float.
# Sample Input:
# [1,2,3,4,5,6,6,6,6,7,7,7]
# 3
# 6
# Sample Output:
# 0.7454545454545455
# Execution Time Limit
# 10 seconds


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
nums=input_list[0]
m=int(input_list[1])
x=int(input_list[2])
from itertools import combinations 
a = 0
b = 0
for c in combinations(nums,m):
    b=b+1
    if x in c:
        a=a+1
    
print (float(a)/b)