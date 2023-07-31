from posixpath import split


a = "hello World"
b = "   hello World"
c = "   hello World     "
# print(a[2])
# print(a[::-1])
# print(a[-9:-6])
# print(a*10)
print(a.capitalize())
print(b.strip())
print(c.lstrip())
print(c.rstrip())
print(a.replace("h","p"))
print(a.count("o"))
print(a.split("h"))
print(a.find("h"))
print(a.find("o",2))
