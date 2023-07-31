a=input(("Enter a number or a word : "))
if(a==a[::-1]):
      print(f"The input {a} is a palindrome")
else:
      print(f"The input {a} Not a palindrome")