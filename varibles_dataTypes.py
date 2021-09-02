"""
Naming Rules
    variable name should be start with underscore/letter(Capital or Samll)
    vairable name can't start with number or can't conatin any notation(@,#,!...)

DataTypes ==> Integer, Float, String,List,Tuple , Dictionary
"""


_name = "Fahad"
age_21 = 21

print(age_21, " " ,_name)
name1 , age = "Ali Tariq" ,25
print (name1 ,age)
# del name1 ,age
# print (name1)
# print( age)

# Number
  # Integer
a = 1
b=999999999999999999999999999999
print(type(b))
  # Float
a = 1.2
b = 3.333333333333333333333333
print(type(b))
  # complex (a+bi)
a = 3 + 5j
b= 3j
print (a ,type(a))
print (b ,type(b))
# String
name = "Fahad"
age = 21
a = "Hello! My name is "
print(a , type(a))
print( "access Specific Element of String " + a[0])
print(a[0:6])
print(a[:])
# a[0]="T" # give us an Error string is imuteable
print( "My name is %s and i'm %d years old"%(name,age))
print( f"My name is {name} and i'm {age} years old")
print( "My name is {name} and i'm {age} years old".format(name=name,age=age))
# a = a + a
# print(a)
# List
list = [1,2,4,"Fahad","Umer","Ahmad"]
print(list[::-1])
list[2]=3

# Tuples
tup =(1,2,3,4)
print(tup)
# Dictionaries
# Sets
