input_list = ['soap','sharp','shy','silent','ship','summer','sheep']

# print(input_list[-1])

sp =list(filter(lambda x: x[0]=='s'and x[-1]=='p',input_list))

print(sp)