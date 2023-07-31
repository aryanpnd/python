# Dictionary Coding
# Description
# Write code to fetch the profession of the employee with Employee id - 104 from an employee input given in the form of a dictionary where key represent employee id and values represent the name, age, and profession (in the same order).



# Sample input:

# Employee_data = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}



# Sample output:

# 'Product Lead'



# Note: Assume that employee data would be available in the data provided to you.

# -----------------------------------------------------------------------------------------------

import ast,sys
input_dict =  { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}

a = input_dict[104]
profession=a[2]

print(profession)