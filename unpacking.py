a,b = 1,2

print(a,b)

c,d =[3,4]

print(c,d)

e,f = (5,6)

print(e,f)

#list to tuple


(g,h,i) = [12,34,56]

print(g,h,i)

mytuple = (1,2,3,4,5)

print(mytuple)

print(list(mytuple))

a,*b ,c= 1,2,3,4,5,6,7,8,9 # this is not arguments

print(a,b,c)

i,*j,k,(a,*b,c)=[1,2,3,4,5,6,7,8,9,"wai","yan","ling"]


print(i,j,k,a,b,c)

mylist = [1,2,3,4,5,6]

yourlist =[7,8,9]

ourlist = [mylist,yourlist]

print(ourlist)

ourlist =[*mylist,*yourlist]

print(ourlist)