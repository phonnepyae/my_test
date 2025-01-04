mylist =[0,1,2,3,4,5,6,7,8,9]

print(mylist[0:-1])

print(mylist[:])

print(mylist[:-3])

mysum = sum(mylist)

print(mysum)

mylist[3] = "a"

print(mylist)


#mylist.reverse()

mylist.remove("a")

print(mylist)


#print(mylist.sort(reverse = False))
mylist.sort(reverse=True)
print(mylist)

mylist_1 = ['e','a','b','c','d']

#mylist.reverse()

print(mylist_1)

mylist_1.sort(reverse=True)

print(mylist_1)

mylist.extend(mylist_1)

print(mylist)

def myfun(*a):
  print("This is from a")
  print(a)
  
  for b in a:
    print(b)
  
  c = list(a)
  for d in c:
    print(d)
  
myfun(mylist_1)


def myfun_1(a,b,c,d,e):
  
  print(a)
  print(b)
  print(c)
  print(d)
  print(e)



myfun_1(*mylist_1)


iterator = iter(mylist)

print(next(iterator))