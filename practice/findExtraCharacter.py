# Find Extra Character
# Description
# Given two strings, one of the strings will contain an extra character. Find the extra character. The number of all the other characters in both the strings will be the same. Check the sample input/output for more clarification.



# The code will be case-sensitive.



# ----------------------------------------------------------------------

# Input:

# Two strings on two separate lines.



# Output:

# One character which is extra in one of the strings.



# ----------------------------------------------------------------------

# Sample input:

# abcd

# cedab



# Sample output:

# e

# Execution Time Limit
# 10 seconds


s1 = input()
s2 = input()


if len(s2) > len(s1):
    longer = s2
else:
    longer = s1

for i in longer:
    if s1.count(i)!=s2.count(i):
        print(i)
        break