a = input("Please enter something  :: ")

  
b = input("Please enter something again :: ")

myList = [1,2,3,4,5,6,7,8,'wai','ling']

if a is b :
  print("They are the same")
  
  
else:
  print("They are not the same")
  
if a in myList:
  print(f"{a} is in list")
  
else:
  myList.append(a)
  
  print(myList)
  
  
if b  in myList:
  print(f"{b} is in list")
  
else:
  myList.append(b)
  
  print(myList)
  