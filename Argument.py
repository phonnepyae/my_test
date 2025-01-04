#positional arguments
#arbitrary arguments
#end of positional arguments => *
#keyword only arguments => key = value
#keyword arguments => **

def myfun(a,b,c,d,*e,f,**g):
  print(a)
  print(b)
  print(c)
  print(d)
  print(e)
  print(f)
  print(g)
  
  #print(h)
  
  
  
myfun(1,2,3,4,5,6,7,8,9,f="hello",g =3)
