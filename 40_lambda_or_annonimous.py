import inspect


x = lambda x,y:x*y

print(x(2,3))


a = lambda x,*args,y,**keywon:print(x,args,y,keywon)


a(1,2,3,4,5,6,y=21,a=1,b=2,c=3)

print(inspect.getsource(a))
print(inspect.getmodule(a))

print("This is a function or not",inspect.isfunction(a))

print(a.__code__.co_argcount)

print(a.__code__.co_filename)

print(callable(a))