myList = [1,2,3,4,5,'kyaw','Hein']

count = 0
for a in range(len(myList)):
  print(a)
  b = myList[a]
  if b is int:
    print(myList)
    
  else:
    myList.pop(count)
  count += 1
    
    
print(myList)