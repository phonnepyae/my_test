import time

def counter(fun,*args,count = 1,**keyword):
  start_time = time.perf_counter()
   
  for i in range(count):
    
    fun(*args,**keyword)
    
  end_time = time.perf_counter()
  whole_time = end_time-start_time
  avg_time   = (end_time-start_time)/count
  print("The whole time is ",whole_time)
  print("The average time is ",avg_time)
def fun(*args,**key):
  
  print("This is arguments => ",args)
  print("This is keyword only argument => ",key)
  
  
counter(fun,1,2,3,4,5,6,count = 5,keyword="hello")





