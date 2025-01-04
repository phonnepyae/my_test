import functools


mylist = [1,2,3,4,5,6]
myReduce = functools.reduce(lambda a,b : a+b ,mylist)

print(myReduce)