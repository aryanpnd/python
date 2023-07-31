# Question 2 LPU03
# Description
# Write a Python program to insert the ‘&’ character in between every character of a string.



# Hint: Make use of a certain built-in function.





# Input : Python



# Output : P&y&t&h&o&n

# Execution Time Limit
# 20 seconds


a = input()
b=""
for i in a:
    i = i + "&"
    b +=i
print(b[:-1])
    