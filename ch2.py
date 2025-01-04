a = 0
b = 0
for a in range(5):
  for b in range(a):
    print("*",end="")
  print("")
for c in range(5):
  for d in range(5-c):
    print("*",end="")
  print("")
