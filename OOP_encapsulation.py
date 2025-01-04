class Parent:
  
  def __init__(self,name,age,roll_number,year):
    
    self.name = name
    self.age = age
    self.roll_number = roll_number
    self.year = year
    
    
class Student(Parent):
  
  def privatedData(self,name,age,roll_number,year):
    
    self.__name = name
    self.__age  = age
    self.__roll_number = roll_number
    self.__year = year
    
  def protectedData(self,year):
    self._year = year
    
  def get_data(self):
    
    print(self.__name,self.__age,self.__roll_number,self.__year)
    
    
student_1 = Student("maung",16,3,"Third_year")

student_1._year = "second year"

print(student_1._year)
  
  

print(student_1.__dict__)

student_1.privatedData("Aung",21,5,"third_year")

print(student_1.__dict__)

student_1.get_data()


  
  