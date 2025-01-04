import pymongo

try:
  my_connection = pymongo.MongoClient("localhost",27017)
  my_db = my_connection["my_testdb2"]
  my_collect = my_db["my_collection"]
  print("Connection is successful!")
  
  
except Exception as err:
  print(err)
  
  
insert_data = {"_id":528,"name":"waiyanling","age":21}

try:
  result = my_collect.insert_one(insert_data)
  print("Insertion is successful!")
  
  print("_ids ... ",result.inserted_id)
  
  _find = my_collect.find().distinct("name")
  
  print("name ... ",_find)  
except Exception as err:
  print(err)