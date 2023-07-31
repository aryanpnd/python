# List of Values in a Dictionary.
# Description
# Create a SORTED list of all values from the dictionary input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple', 'Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}



# Sample Input:

# {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple', 'Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}



# Sample Output:

# ['Amazon', 'Apple', 'RJIO', 'Twitter']

# -----------------------------------------------------------------------------------------------

import ast,sys
input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple', 'Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

a = input_dict.values()
b = list(a)
b.sort()
print(b)

