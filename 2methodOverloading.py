class Price:
  
  def payment(self,a = None,b = None,*c):
    
    print("We will take only first two arguments")
    
    if a != None and b != None :
      return a * b
    
    elif a != None:
      return a
    
    else:
      return None
    
class Price_1:
  def payment(self,*args):
    data = 0
    count = 0
    for i in args:
      count += 1
      data = data + i
    print("There is {0} time for counting".format(count))
    return data
    

obj = Price()
obj2 = Price_1()




print(obj.payment(12,2))

print(obj.payment(1,2,3,4,5,6,7,8,9))

print(obj2.payment(1,2,3,4,5,6,7,8,9))