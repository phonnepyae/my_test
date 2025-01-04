import pymongo

try:
  my_connection = pymongo.MongoClient("localhost",27017)
  my_db = my_connection["my_testdb2"]
  my_collect = my_db["my_table"]
  
  print("Connection is successful!")
  
except Exception as err:
  
  print("Something wrong!")

print("< find method >")  
try:
  
    result = my_collect.find()
    print(result)
    
    for data in result:
      print(data)
    
    
except Exception as err:
    
    print(err)
    
    
print("< find({},{}) >")

try:
  
  _find = my_collect.find({},{"name":1})
  
  for db in _find:
    print(db)
    
  
except Exception as err:
  print(err)
  
  
print("< $ method >")

query = {"name":{"$lt":"H"}}

result1 = my_collect.find(query)

for i in result1:
  print(i)
  

print("< regex method >")

regex = {"name":{"$regex":"^A "}}

result_rg = my_collect.find(regex)

for d in result_rg:
  print(d)