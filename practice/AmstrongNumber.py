# Armstrong Number
# Description
# Any number, say 'n', is called an Armstrong number if it is equal to the sum of its digits, where each is raised to the power of the number of digits in 'n'.

# For example:

# 153=13+53+33



# Write a Python code to determine whether an entered three-digit number is an Armstrong number or not. 

# Assume that the number entered will strictly be a three-digit number.

# Print "True" if it is an Armstrong number and print "False" if it is not.

# Sample Input:

# 153

# Sample Output:

# True

# Execution Time Limit
# 10 seconds


a = int(input("enter a number : "))
b = len(str(a))
var1 = a
sum1 = 0
while var1>0:
  digit = var1%10
  sum1 = sum1 + digit**b
  var1 = var1//10

if a == sum1:
  print("True")
else:
  print("False")

