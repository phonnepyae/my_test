def outer_fun(fun):
  
  from functools import lru_cache
  
  @lru_cache(maxsize= 10)
  
  def inner(*args):
    n,*arg= args
    result = fibo(n)
    
    return result
  
  return inner

@outer_fun

def fibo(n):
  print("Calculating ..... ",n)
  return 1 if n<3 else fibo(n-1)+fibo(n-2)

print(fibo(5))