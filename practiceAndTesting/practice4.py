# Python Loops
# Python has two primitive loop commands:

# while loops
# for loops
# ----------------------------------------------------------------------------------------

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# -------------------------------------------------------------------------------------------------
# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
  print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
for x in range(6):
  print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
# Using the start parameter:
for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

