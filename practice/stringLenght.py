# Longest Word in a String
# Given a sentence as a string, find out and print the length of the longest word present in it.

# Note: The string just contains alphabets and white spaces. There won't be any special characters like periods, commas, hyphens etc.

# Examples:
# Input 1:
# I love Python
# Output 1:
# 6

s = input()

s = str.split(s,' ')
longest = 0
for i in s:
    if len(i) >longest:
        longest = len(i)
print(longest)