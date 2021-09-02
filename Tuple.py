tup = (1 , 10 , 13 , 42 , 5 , 0 , 7 , 8)

print(

  "tuple \t\t", tup,
  "\nAccess 0 Element\t\t", tup[0],
  "\nAccess first 5 Element\t\t", tup[0:5],
  "\nAccess last 3 Element\t\t", tup[-3:],
)

print(
  sorted(tup),"\n",
  max(tup),"\n",
  min(tup),"\n",
  all(tup),"\n",
  any(tup),"\n",
  tuple("Fahad")
)
