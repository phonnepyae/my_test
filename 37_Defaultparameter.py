

def bshop(name:'book name',quantity:'number of book',unit:'unit',tlist = None,blist = None)->"return book list in each store":
  
  
  """This is book shop store list"""
  
  blist = []
  
  blist.append(name)
  blist.append(quantity)
  blist.append(unit)


  if not tlist:
    tlist = []
    
  tlist.append(blist)
  return tlist


  
  
store1 = bshop("python",3,"book")

bshop("jave",3,"book",store1)

store2 = bshop("love",3,"book")

bshop("wai yan ling",1500,"love",store2)

print(store1)

print(store2)


help(bshop)


print(bshop.__annotations__)

print(bshop.__doc__)