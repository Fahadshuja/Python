

lis = [1 , 2, 3 , "My" , "Name" , "is" , "Fahad" , 21.0 , 3j]

print ("list",lis)


print("list Slicing",lis[0:5])

print(lis[:-2])
print(lis[6])
print(lis[-1])
lis[-1] = "Python"
print(lis)

del lis[-1]

print(lis)


multi_lis = [[1 , 2 , 3],["Umer" , "Ahmad" , "Fahad"]]

print(multi_lis)

print(multi_lis[::-1])

print(multi_lis[1][0])

a = [1 , 4 , 7 , 3 , 2]
b = [4 , 5 , 6]
lis_concat=a + b

print("list concatination ==>",lis_concat,
      f"\n Operation on List a = {a} * 3 ==>",a *3)

print(f"\n2 in {a}", 2 in a)

# Builtin

print (
        "max\t" ,max(a)
       ,"\nmin\t" ,min(a)
       ,"\nsort\t" , sorted(a)
       ,"\nlen\t" ,len(a)
       ,"\nsum\t" , sum(a)
       ,"\nall\t" ,all(a)
       )


print (list("21"))


# traversing of List
for i in a:
  print (i)


# Builtin Method

a.append("this")
a.insert(0,"Aadi")
print(a)
a.insert(2,2)
# a.remove(2)
print(a.count(2))
print(a)



# list Comprehenssion

even= [ i for i in range(0,10) if i%2==0]
print(even)
