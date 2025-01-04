import pymysql as my_sql

my_db = my_sql.connect(
  
  host = "localhost",
  user = "root",
  passwd = "toor"  
)

my_cursor = my_db.cursor()

#my_cursor.execute("CREATE DATABASE mytest_db")

my_cursor.execute("SHOW DATABASES")

#for db in my_cursor:
  #print(db)
  
  
for db in my_cursor:
  print(db[0])