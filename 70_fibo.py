def decorator(fun):
  
  from functools import wraps
  cache = {1:1,2:1}
  @wraps(fun)
  def inner(n):
    if n not in cache:
      cache[n] = fun(n)
    
    return cache[n]
  
  return inner
  
    


@decorator
def fibo(n):

  print("calculating the fibo => ",n)
  
  return 1 if n<3 else fibo(n-1)+fibo(n-2)

print(fibo(10))

print(fibo(5))