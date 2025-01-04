def reFun(m):
  
  if m == 1:
    return squre
  
  else:
    return cube


def squre(n):
   
   ans = n**2
  
   return ans
   
def cube(n):
   
   ans = n**3
   return ans
   
   
a = reFun(1)

print(a(2))