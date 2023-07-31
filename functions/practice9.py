from functools import reduce
import functools

input_list = ['All','you','have','to','fear','is','fear','itself']

final_str = reduce(lambda x,y: x + " " + y,input_list)


print(final_str)