# Iterations
# Description


# You are given a list of string elements and asked to return a list which contains each element of the string in title case or in other words first character of the string would be in upper case and remaining all characters in lower case



# Sample Input:



# ['VARMA', 'raj', 'Gupta', 'SaNdeeP']







# Sample Output



# ['Varma', 'Raj', 'Gupta', 'Sandeep']

# -------------------------------------------------------------------------------------------



import ast,sys
input_list = ['VARMA', 'raj', 'Gupta', 'SaNdeeP']
output_list = []
for i in input_list:
    str(i)
    b = i.capitalize()
    output_list.append(b)

print(output_list)
# print(output_list)