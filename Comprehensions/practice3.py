# USING FOR LOOP
ordinary_dict ={}

for i in range(2,21):
    if i % 2 == 0:
        ordinary_dict[i] = i**2

print(ordinary_dict)


# USING COMPREHENSION
updated_dict = {i : i**2 for i in range(2,21) if i % 2 ==0}
print(updated_dict)