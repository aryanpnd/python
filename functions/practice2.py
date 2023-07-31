def list_diff(list1,list2):
    list3 = []
    for  i in range(0, len(list1)):
        list3.append(list1[i] - list2[i])
    return list3

L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]

print(list_diff(L1, L2))