input1 = input("Please enter something :: ")

input2 = input("Please reenter above :: ")

print("Input1 location :: ",id(input1))

print("Input2 location :: ",id(input2))

if id(input1) == id(input2): 
  
  #String cannot have the same memory location
  
  print("They have same memory location ")
  
  
else:
  print("They are not the same location")
  
  
if input1 is input2:
  print("They are the same ")
  
else:
  print("They are not the same")