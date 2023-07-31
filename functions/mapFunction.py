# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

print("-"*60,"\n USING A LAMBDA FUNCTION \n")

list_numbers = (1,2,3,4)
sample_map = map(lambda x: x*2, list_numbers)
print(list(sample_map))


print("-"*60,"\n USING A FUNCTION \n")


def multi(x):
    return x*2

list_numbers = [1,2,3,4]
sample_map = map(multi, list_numbers)

print(list(sample_map))