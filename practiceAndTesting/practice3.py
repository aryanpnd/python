# data types in python
# 4 built-in data types in Python used to store collections of data, they are List, Set,tuples, and Dictionary, all with different qualities and usage.

#tuples

mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# List
# Lists are used to store multiple items in a single variable.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Set
# Sets are used to store multiple items in a single variable.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)