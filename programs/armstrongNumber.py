a = int(input("enter a number : "))
b = len(str(a))
var1 = a
sum1 = 0
while var1>0:
  digit = var1%10
  sum1 = sum1 + digit**b
  var1 = var1//10

if a == sum1:
  print(f"{a} is an armstrong number")
else:
  print(f"{a} is not an armstrong number")