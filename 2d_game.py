import secrets

count1 = 1
count2 = 1
secure_number = secrets.SystemRandom()


while count1 == 1:
  
  user_name = input("Enter your name at least 6 words == ")
  
  user_age = int(input("Enter your age == "))
  
  if (len(user_name)>5 and user_age > 17):
    print("***Welcome out game site***")
    

    while( user_age > 18 ):
      
     press1 = int(input("""press 1 for regulations of the  game 
press 2 for  playing game
press any number  for leaving the game"""))
       
     if (press1 == 1 ):
      
        print("""You can play the game above 5000 kyats.
You are above 18 year old
If you start playing the game,you can leave the game above your money 10000kyats.""")
      
     elif (press1 == 2 ) :
 
        
        while(count2 == 1):
          
          show_money = int(input("Please enter your amount :: "))
          user_input = int(input("press any number to continue or Press 1 to exit"))
          if(user_input == 1):
             count2 = 0
             press1 = 1 
          else:
             print("You are welcome!")
             
         
          while(show_money > 4999):
            counter = 1
            if counter > 1:
                user_input = int(input("press any number to continue or Press 1 to exit"))
                if(user_input == 1):
                  count2 = 0
                  press1 = 1 
                else:
                 print("Good luck!")
               
            else:
               print("")
              
            try:
              user_num = int(input("Please enter yor lucky number :: "))
              
              
                
          
              if(user_num > 99 and user_num <1000):
            
          
                play_amount = int(input("Please enter your money to play the game for one round ::"))
          
                time_num = int(input("Please enter your time for one round from 10 to 100 time :: "))
          
                if(time_num >10 and time_num < 101):
            
                  generated_num = secure_number.randrange(100,999,user_num)
              
                  if(user_num == 123):
                    print("You win the game !")
                    prize = play_amount*time_num
                    print("Your prize amount is {}Kyats. ".format(prize))
                    show_money = show_money+ prize
                    print("Your total money is ",show_money)
                    counter = counter +1
                
                  else:
                    print("Oop!,try again.") 
                    user_input = int(input("press any number to continue or Press 1 to exit"))
                    if(user_input == 1):
                      count2 = 0
                      press1 = 1 
                    else:
                      continue
                    
                            
              
              
                else:
              
                  print("Please enter between limit number!")
            
              else:
                print("Please enter only 3 digits !")         
          
          
         
          
            except ValueError:
            
              print("Please enter only number!")
          
          print("Please enter above 5000kyats!") 
          
          user_input = int(input("press any number to continue or Press 1 to exit"))
          if(user_input == 1):
             count2 = 0
             press1 = 1 
          else:
             continue
            
     else: 
        print("Good luck!")
        
        user_age = 1
        count1 = 0
      
      
  else:
    print("""Your name must be more than 5 words or 
your age must be 18 year old  to play the game""")     
      

      
      
     
      
    
     