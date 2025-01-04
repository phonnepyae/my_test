class People:
   def __init__(self, id, age):
      self.id = id
      self.age = age
      
   def __add__(self,self1,self2):
     total_id = self.id + self1.id + self2.id
     total_age = self.age + self1.age + self2.age
     return total_id,total_age
     
      
p1 = People(101,23)
p2 = People(102,24)
p3 = People(103,24)

total_p = p1 + p2 + p3

print(total_p)