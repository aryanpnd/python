# Type of Triangle
# You're given a tuple with 3 integers representing the three sides of a triangle. Based on the three sides you need to determine the type of triangle based on both angles and sides, i.e. Acute, Obtuse, or Right angled triangle along with Equilateral, Isosceles, or Scalene. See examples for more details.

# Format:
# Input: A single tuple containing three integer values.
# Output:  A string telling the type of triangle. First print the type of triangle based on the angles and then based on the sides. So if a triangle is, say, acute and scalene, you need to print 'Acute' on the first line and 'Scalene' on the second line. If the sides are such that a triangle cannot be formed, print 'Invalid'. You need to print the following strings for each of the cases:
# Acute angled triangle: 'Acute'
# Right angled triangle: 'Right'
# Obtuse angled triangle: 'Obtuse'

# Equilateral triangle: 'Equilateral'
# Isosceles Triangle: 'Isosceles'
# Scalene Triangle: 'Scalene'

# Examples:
# Input 1:
# (4, 9, 10)
# Output 1:
# Obtuse
# Scalene
# Input 2:
# (3, 8, 12)
# Output 2:
# Invalid

# Explanation: In the first example, the triangle is obtuse according to the angles and since the three sides are unequal, it is a scalene triangle.
# In the second example, the 3 values are not satisfying the condition a+b < c, where c is the largest size. Hence, a triangle cannot be formed using these three sides which means the given input is 'Invalid'.


# # Read the input list
# import ast,sys
# input_str = sys.stdin.read()
# t = ast.literal_eval(input_str)

# t = sorted(t)

# def side_func(t):

#     if(t[0] + t[1] <= t[2]):
#         return('Invalid')

#     elif(t[0] == t[1] and t[1] == t[2]):
#         return('Equilateral')

#     elif((t[0] == t[1]) or (t[1] == t[2]) or (t[0] == t[2])):
#         return('Isosceles')
#     else:
#         return('Scalene')
        
# def angle_func(t):
#     if(t[2]**2 == t[0]**2 + t[1]**2):
#         return('Right')
        
#     elif(t[2]**2 < (t[0]**2 + t[1]**2)):
#         return('Acute')
        
#     else:
#         return('Obtuse')
        
# side = side_func(t)
# angle = angle_func(t)

# if(side=='Invalid'):
#     print(side)
# else:
#     print(angle)
#     print(side)