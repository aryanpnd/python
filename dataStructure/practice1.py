input_str= input()
message1=input_str[0::2]
message2=input_str[1::2]
if len(message1)<len(message2):
    print(message1+"#"+","+message2)
if len(message1)>len(message2):
    print(message1+","+message2+"#")
else:
    print(message1+","+message2)