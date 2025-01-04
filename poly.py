#polymorphism => same method with different class

class Student_1:
  
  def human(self):
    
    print("Student_1 is roll number one.")
    
    
class Student_2:
  
  def human(self):
    print("Student_2 is roll number two.")
    

class Student_3:
  
  def human(self):
    print("Student_3 is roll number three.")
    
    
    
class Person:
  
  def get_data(self,obj):
    
    obj.human()
    
phyu = Student_1()

people = Person()

people.get_data(phyu)