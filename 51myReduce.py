def mysum(a,b):
  
  return a+b


def myReduce(mysum, mylist):
  
  first = mylist[0]
  for i in mylist[1:]:
    first = mysum(first,i)
    
  return first

mylist = [1,2,3,4,5,6,7]
print(myReduce(mysum,mylist))