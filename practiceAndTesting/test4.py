def new_func():
    for i in range(1,5):
        print(i)
    return new_func()

print(new_func())