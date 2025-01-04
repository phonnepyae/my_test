class Price:
  def payment(self, a = None ,b = None):
    
    if a != None and b != None :
      return a * b
    
    elif a != None:
      return a
    
    else:
      return None
    
obj = Price()

print(obj.payment(10))

print(obj.payment(10,20))