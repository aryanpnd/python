input_str= input()
message1=input_str[0::2]
message2=input_str[1::2]
if len(message1)<len(message2):
    print(message1+"#"+","+message2)
if len(message1)>len(message2):
    print(message1+","+message2+"#")
else:
    print(message1+","+message2)

# a = "this is a string"# here we are declaring a variable of string

# print(a.strip("#")) 


# x = ((1,2,3), 4,5)
# print(type(x))