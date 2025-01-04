import pymongo

try:
  my_connection = pymongo.MongoClient("localhost",27017)
  my_db = my_connection["my_testdb2"]
  my_collect = my_db["my_table"]
  
  print("Connection is successful!")
  
except Exception as err:
  
  print("Something wrong!")
  
insert_datas =[ {"_id":1,"name":"Phonne Pyae"},
                {"_id":2,"name":"Phonne"},
                {"_id":3,"name":"Pyae"},
                {"_id":4,"name":"Kyaw kyaw"},
                {"_id":5,"name":"Maung Maung"},
                {"_id":6,"name":"Aung Aung"}
                ]

try:
  
  result = my_collect.insert_many(insert_datas)
  
  _ids = result.inserted_ids
  
  print("_ids ... ",_ids)
  
except Exception as err:
  
  print(err)