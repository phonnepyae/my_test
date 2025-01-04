
user_input1 = input("Please enter first number :: ")
user_input2 = input("Please enter second number :: ")
input3 = input("Please enter operator ::  + , - , * ,/  =>  ")

try:
  input1 = int(user_input1)
  input2 = int(user_input2)
  if input3 == "+":
     print("Answer :: ",input1+input2)
    
  elif input3 == "-":
     print("Answer :: ",input1-input2)
     
  elif input3 == "*":
     print("Answer :: ",input1*input2)
     
  elif input3 == "/": 
    print("Answer :: ",(input1/input2))
    
  else:
    print("Please enter operator!")
    
  
  
  
except ValueError:
  print("Please enter integer only!")
  
  
except ZeroDivisionError:
  print("Zero division error!")

