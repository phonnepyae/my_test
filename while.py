
count = 0
a = False
press = 0
while count < 3:
  while a == False:

   user_input1 = input("Please enter your password between 10 characters :: ")

    
   if len(user_input1)>10:
       print("You enter more than 10 characters!")
      
   else:
      a = True
      continue
         
  user_input2 = input("Confirm your password :: ")
  
  try:
  
    if (user_input2 == user_input1) :
      
      print("Welcome")
      count = 4
      
      
    else:
      count = count + 1
      
      print("Not match two passwords!")
      print('Yor wrong time is ',count)
      if count == 3:
        print("Try again after 3 mins")
      
      else:
       press = input("Press '1' to show your password  => ")
       if press == "1":
        print("Password =>  ",user_input1)
       else:
         continue
  
       
  except ValueError:
     print("Something wrong!")
  