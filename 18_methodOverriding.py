class Parent:
  
  def inheritance(self):
    
    print("This is from parent class.")
    
    
class Child(Parent):
  
  def inheritance(self):
    
    print("This is from child class.")
    
class Grandchild(Child):
  
  def inheritance(self):
    
    print("This is from grandchild class.")
    
    
obj = Grandchild()
obj.inheritance()