import ast,sys
from parser import tuple2st
input_tuple = ('Monty Python', 'British', 1969)

# Write your code here
input_list = list(input_tuple)
input_list.append("Python")
tuple_2 = tuple(input_list)
# Make sure to name the final tuple 'tuple_2'
print(tuple_2)
