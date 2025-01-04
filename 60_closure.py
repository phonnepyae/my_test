
def outer_fun():
  
  data = "This is from closure function"
  
  def inner_fun():
    print(data)
  
  return inner_fun

fun_obj = outer_fun()

del outer_fun

fun_obj()

def outer(fun):
  
  def inner(*args):
    
    print(fun(*args))
    
  return inner
  
  
def add(*arg):
  data = 0
  for i in arg:
    data += i
    
  return data

def multi(*arg):
  data = 1
  for i in arg:
    data = data*i
  return data
  
fun_obj1 = outer(add)
fun_obj1(1,2,3,4)
fun_obj1 = outer(multi)
fun_obj1(1,2,3,4)

fun_obj1(1,2,3,4,5)