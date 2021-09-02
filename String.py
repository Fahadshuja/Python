# String in=s Imutable
str = "My name is Fahad."

print(str)

# Select single ELement
str[0]

# Deletion & Updation of Single Elemet is not Allowed

# Formating of String
a = "Hello!"
b = 22
# .format()
print ("{0} {1} {2}".format(a,str,b))
# %s  %d  %f
print("%s %s %d"%(a , str , b))
# f"String"
print(f"{a} {str} {b}")

# Operation on String

print( "Addition", a + a)

# print( "Add string to a number", a + 21) #give us an TypeError of

print( "Addition", a * 2)

# method Of String
# len
print("len",len(a))
#strip  //remove blank Spaces from both front and end f String
a ="hello! llo "
print(a.strip())
# find give the first index of find item else return -1
print(a.find("llo",7))
# join
print("".join(["1","2","3"]))


