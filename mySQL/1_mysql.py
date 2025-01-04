import pymysql 


connection = pymysql.connect(
  
host = "localhost",
user = "root",
password = "toor" )

print(connection)

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
  
  print(db[0])
  
cursor.close()
connection.close()