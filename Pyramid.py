
user_input = int(input("Please enter no of row :: "))

size = user_input
for i in range(user_input):
  
  for j in range(1,size):
    print(end=" ")
  size = size - 1
    
  for k in range(1,i*2):
    print(end="*")
    
  print("")