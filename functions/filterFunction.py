# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

print("-"*60,"\n Vowels program \n")


# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)

# --------------------------------------------------------------------------------------
print("-"*60,"\n Odd and Even number program \n")

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
  
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
