# runner up question

n = int(input())
arr = map(int, input().split())
sortList = set(arr)

x = sorted(sortList,reverse=True)
print(x[1])