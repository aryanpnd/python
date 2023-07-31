# List Overlap LPU 05
# Description
# Write Python code to find elements common between the two lists. 
# The output list should exclude duplicate elements. i.e. if both lists have 1 twice then the output list should have 1 only once.
# The input will contain two lines with two lists.
# The output should contain a list of common elements between the two input lists.
# Sample Input:
# [1,2,3,4,5]
# [4,5,6,7,8]
# Sample Output:
# [4, 5]

# Execution Time Limit
# 10 seconds

import ast,sys
input_str = sys.stdin.read()
inp = ast.literal_eval(input_str)
list1=inp[0]#first list
list2=inp[1]#second list

list3 = []
for i in list1:
    if i in list2:
        list3.append(i)

print(list3)