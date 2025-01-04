
def outer_fun():
  
  var = "Wai"
  
  print("Before passing funs => ",var)
  
  def inner_fun1():
  
    def inner_fun2():
      
      print("This is from inner_fun2 => ",var)
      
    inner_fun2()
    
    nonlocal var
    var = "Yan"
    print("This is from inner_fun2 => ",var)
    
  inner_fun1()
  print("After passing funs => ",var)
  
outer_fun()