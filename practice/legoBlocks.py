# Lego Stack
# Description
# You are given a row of Lego Blocks consisting of n blocks. All the blocks given have a square base whose side length is known. You need to stack the blocks over each other and create a vertical tower. Block-1 can go over Block-2 only if sideLength(Block-2)>=sideLength(Block-1).



# From the row of Lego blocks, you can only pick up either the leftmost or rightmost block.

# Print "Possible" if it is possible to stack all n cubes this way or else print "Impossible".



# Input Format:

# The input will contain a list of n integers representing the side length of each block's base in the row starting from the leftmost.



# Sample Input:

# [5 ,4, 2, 1, 4 ,5]

# Sample Output:

# Possible

# Execution Time Limit
# 10 seconds


sides = [5 ,4, 2, 1, 4 ,5]
n = len(sides) 

my_stack = []
i = 0

while(i < n):
    if sides[i] >= sides[n-1]:
        my_stack.append(sides[i])
        i = i+1
    else:
        my_stack.append(sides[n-1])
        n = n - 1
flag = 0
i = 1
while i < len(my_stack): 
    if(my_stack[i] > my_stack[i - 1]): 
        flag = 1
    i += 1


if (not flag) : 
    print ("Possible") 
else : 
    print ("Impossible") 