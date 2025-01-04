
g = 1

def fun(n):
  global g
  g = 2
  result = g*n
  
  return result

print(fun(3)) 
print(g)


def outer_fun():
  
  var = "hello"
  
  def inner_fun1():
    
    var = "world"
    
    print("This is from inner_fun => ",var)
    
  inner_fun1()
  
  print("This is from outer_fun => ",var)
    
    
outer_fun()
   
   



