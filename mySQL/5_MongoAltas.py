

from pymongo.mongo_client import MongoClient

uri = "mongodb://root:toor@cluster0-shard-00-00.zdory.mongodb.net:27017,cluster0-shard-00-01.zdory.mongodb.net:27017,cluster0-shard-00-02.zdory.mongodb.net:27017/?ssl=true&replicaSet=atlas-xgnjq4-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)


try:
   
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
my_db = client["mytest_db"]
my_collect = my_db["my_collection"]

data = {"_id":1,"name":"waiyanling","age":21}

my_collect.insert_one(data)