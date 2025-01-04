import pymongo



try:
  my_connection = pymongo.MongoClient("localhost",27017)
  my_db = my_connection["my_testdb3"]
  my_collection = my_db["Students_info"]
  
  print("Connection is successful!")
  
  

except Exception as err:
  print(err)

#old_one = {"Name":"Bob Johnson"}
#new_one = {"$set":{"Name":"Kyaw Kyaw"}}

old_one = {"Age":{"$regex":"^20"}}

new_one = {"$set":{"Age":100}}

try:
   my_collection.update_many(old_one,new_one)
   
   print("Updating is successful!")
   
except Exception as err:
  print(err)