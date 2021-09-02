uservalue = int(input())
if uservalue > 3:
  print("value you enter is greater then 3")
else:
  print("value is less then 3")

print("mested If Else Condition")
if uservalue < 5:
  print("value you enter is less then 5")
if uservalue < 10 and uservalue >=5:
  print("value you enter is greater then or equal to 5 and less then 10")

else:
  print("value is greater then 10")



print("True") if 1 < 2 else print("False")

# netsted if else

print("True") if 1 > 2 else print("False") if 2 > 3 else print("False1")



# with tuple

ternary_tup=("False Tuple","True tuple")[1<2]

print(ternary_tup)


# With Dictionary
ter_dict={False:"Dict False" ,True:"Dict True" }[1<2]

print(ter_dict)
