# using list comprehension
L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
L3 = [L1[i] - L2[i] for i  in range(0, len(L1))]
print(L3)