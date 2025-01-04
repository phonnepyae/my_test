def logger(fun):
  
  from functools import wraps
  from datetime import datetime, timezone
  counter = 0
  @wraps(fun)
  
  def inner(*args,**kwargs):
    
    nonlocal counter
    counter += 1
    dt = datetime.now(timezone.utc)
    result = fun(*args,**kwargs)
    
    print("{0} function is called at {1} for {2} time.".format(fun.__name__,dt,counter))
    
    return result
  return inner

def timer(fun):
  
  from functools import wraps
  from time import perf_counter
  @wraps(fun)
  def inner(*args,**kwargs):
      
    start = perf_counter()
    result = fun(*args,**kwargs)
    end = perf_counter()
    long_time = end - start
    
    print("{0} takes for {1:6f} to run for finding factorial number {2}".format(fun.__name__,long_time,args))
    
    print("The result is ",result)
    return result
  return inner


@logger
@timer


def factorial_num(n):
  from functools import reduce
  from operator import mul
  
  return reduce(mul,range(1,n+1))

factorial_num(5)