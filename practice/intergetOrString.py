# Integer or String
# Description
# You have been using ast.literal_eval() to take input in a suitable format. Have you thought of how it distinguishes between different data types and data structures?



# We will solve a similar but smaller problem here. You will be given a string as input. You will have to determine if the string can be an integer or not.



# This is also encountered a lot in Data Science. Upon taking a lot of data, sometimes integer values are treated as a string, and due to that, a lot of functionalities of integer data that you will learn ahead are rendered useless.



# ----------------------------------------------------------------------

# Input:

# A single line of string.



# Output:

# INT if the input string is an integer and STR otherwise.



# ----------------------------------------------------------------------

# Sample input:

# 12



# Sample output:

# INT



# ----------------------------------------------------------------------

# Sample input:

# 12.4



# Sample output:

# STR



# Explanation: You only have to print INT if it's an integer; in this case, it is a float.



# ----------------------------------------------------------------------

# Sample input:

# 43a



# Sample output:

# STR

# Execution Time Limit
# 15 seconds

# my_str = input()
# print(type(my_str))
# if type(my_str)==str:
#     print("STR")
# elif type(my_str)==float:
#     print("STR")
# else:
#     a=int(my_str)
#     print(a)

str = input()
 
if str.isdigit():
    print("INT")
else:
    print("STR")