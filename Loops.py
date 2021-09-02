# For Loop

for i in range(0,5):
  print (i)

# While Loop
a=0
while(a<10):
  print (a)
  a+=1

# Nested For Loop

for i in [1 , 2 , 3 , 4 , 5]:
  for j in range(1,11):
    print (f"{i} x {j} = ",i*j )

# For Else Loop

for i in "Fahad":
  print(i)
else:
  print ("Loop Reach to end")

# break and Continue Statement

for i in range(0,10):
  if i==5:
    continue
  print("..\t", i)
  if i == 7:
    break
