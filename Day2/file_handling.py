file = open("file.txt" , 'r')
# content = file.read()
# content = file.read(5)
# content = file.readline()
content = file.read(5)
print(content)
print(file.readlines())


file = open("file.txt" , 'r+')
content = file.read()
file.write("Hello! My name is Fahad..")
print(content)


file = open("file.txt" , 'w')
# content = file.read()
file.write("Hello! My name is Fahad..")
# print(content)
file.close()
with open("file1.txt" , "a") as f:
  f.write("\nHello world")

