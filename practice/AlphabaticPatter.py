# Alphabetic Patterns
# Description
# Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern.

 

# Sample Input: 5 

 

# Sample Output : 

# --------e-------- 

# ------e-d-e------ 

# ----e-d-c-d-e---- 

# --e-d-c-b-c-d-e-- 

# e-d-c-b-a-b-c-d-e 

# --e-d-c-b-c-d-e-- 

# ----e-d-c-d-e---- 

# ------e-d-e------ 

# --------e-------- 

 

# Sample Input : 3 

 

# Sample Output : 

# ----c---- 

# --c-b-c-- 

# c-b-a-b-c 

# --c-b-c-- 

# ----c----



# Please note that this question was asked during an interview for the role of a Data Scientist.

# Execution Time Limit
# 25 seconds

import string

n = int(input())

a = string.ascii_lowercase

# Write your code below

List = []

for i in range(n):

    s = "-".join(a[i:n])

    List.append(s[::-1]+s[1:])

width = len(List[0])

for i in range(n-1, 0, -1):

    print(List[i].center(width, "-"))

for i in range(n):

    print(List[i].center(width, "-"))