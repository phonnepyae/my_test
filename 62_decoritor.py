def multi(x,y):
  
  return x*y

def sub(x,y):
  
  return x/y

def dec(fun):
  counter = 0
  def inner(*args):
    nonlocal counter
    counter += 1
    x,y,*arg = args
    if x < y:
      x,y = y,x
    print("The {0} is calling {1} time.".format(fun.__name__,counter))
    return fun(x,y)
  return inner


fun_obj = dec(multi)

print(fun_obj(2,3,4,5))


print(fun_obj(12,4,56,6,7,8,9,0,1))

fun_obj1 = dec(sub)

print(fun_obj1(4,2,3,4,5,6))
      
  