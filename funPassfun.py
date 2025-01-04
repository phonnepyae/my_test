

def funPassfun(fun,*a):
  
  return fun(*a)


def fun(*args):
  
  print(args)

  
  
funPassfun(fun,1,2,3,4,5,6)