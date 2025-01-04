def logger(fun):
  
  from functools import wraps
  from datetime import datetime, timezone
  counter = 0
  def inner(*args,**kwargs):
    nonlocal counter
    counter += 1
    dt = datetime.now(timezone.utc)
    result = fun(*args,**kwargs)
    
    print("{0} function is called at {1} for {2} times.".format(fun.__name__,dt,counter))
    
    
    return result
  return inner

@logger

def my_fun(a,b):
  
  result = a**b
  return result

@logger
def my_fun2(a,b):
   result = a -b
   return result
 
print(my_fun(3,3))

print(my_fun(2,4))

print(my_fun2(1,4))