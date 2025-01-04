myList = [1,2,3,4,5,6,7,8,9,13,234,56,43,2345,236]

max_num = myList[0]

print(max_num)

for a in range(len(myList)):
   if max_num < myList[a]:
     max_num = myList[a]
     
   else:
     max_num = max_num
     
     
print("Maximun number is ",max_num)