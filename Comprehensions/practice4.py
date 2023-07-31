
input_list = ['wood','old','apple','big','item','euphoria']

print("-"*60, "\n")
print("Using For loop")

b = []
for i in input_list:
    if i.startswith("a") or i.startswith("e") or i.startswith("i") or i.startswith("o") or i.startswith("u"):
        b.append(i)
print(b)

print("-"*60,"\n")
print("Using Comprehension")

list_vowel= []
a = [list_vowel.append(i) for i in input_list     if i.startswith("a") or i.startswith("e") or i.startswith("i") or i.startswith("o") or i.startswith("u") ]

print(list_vowel)