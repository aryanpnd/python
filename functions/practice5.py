input_list = ['Santa Cruz','Santa fe','Mumbai','Delhi','San fansico']


count = list(map(lambda x:x[0]=='S',input_list)).count(True)
print(count)
