file = open("example.txt", "r")
  
count = 0
while True:
    
    # this will read each character
    # and store in char
    char = file.read(1)
    print(char)
      
    if char == " ":
        count += 1
    if not char:
        break
  
print(count)