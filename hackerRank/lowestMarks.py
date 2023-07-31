if __name__ == '__main__':
    dict1 = {}
    for _ in range(int(input())):
            name = input()
            score = float(input())
            dict1.update({name:score})

    a = sorted(dict1.values())
    value = {i for i in dict1 if dict1[i]==a[1]}
    for i in value:
        print(i)


# Result =[]
# scorelist = []

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         Result+=[[name,score]]
#         scorelist+=[score]
#     b=sorted(list(set(scorelist)))[1] 

#     for a,c in sorted(Result):
#         if c==b:
#             print(a)