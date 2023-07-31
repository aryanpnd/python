# Second Maximum Number in a List
# Description
# Given a list of numbers, find the second largest number in the list.



# Note: There might be repeated numbers in the list. If only one number is present in the list, return 'not present'.



# Examples:

# Input 1:

# [7, 2, 0, 9, -1, 8]

# Output 1:

# 8



# Input 2:

# [3, 1, 4, 4, 5, 5, 5, 0, 2, 2]

# Output 2:

# 4



# Input 2:

# [6, 6, 6, 6, 6]

# Output 2:

# not present

# Execution Time Limit
# 15 seconds


input_list = [7, 2, 0, 9, -1, 8]


input_set = set(input_list)
my_list = sorted(list(input_set))

if len(input_set) < 2:
    print("not present")
else:
    print(my_list[-2])