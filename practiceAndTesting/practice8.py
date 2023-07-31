import random

print(random.random())
print(random.randint(1,100))
print(random.randrange(1,10))
print(random.randrange(0,10,2))  # for even numbers
print(random.randrange(1,10,2))  # for odd numbers
print(random.uniform(1,10))
print(random.sample(range(1,10),5))
# -----------------------------------------------------------
list1 = ["aryan","aditya","amir","benjamin","mujtafa"]
random.shuffle(list1)
print(list1)
#------------------------------------------------------------
# -----------------------------------------------------------
list2 = ["aryan","aditya","amir","benjamin","mujtafa"]
print(random.choice(list2))

#------------------------------------------------------------

