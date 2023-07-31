input_list = [65,76,87,23,12,90,99]
from functools import reduce

answer = reduce(max,input_list)

print(answer)