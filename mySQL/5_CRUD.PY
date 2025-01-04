import pymysql

my_db = pymysql.connect(
  host = "localhost",
  user = "root",
  passwd = "toor",
  database = "mytest_db" 
)

my_cursor = my_db.cursor()

#my_cursor.execute("CREATE TABLE my_table2(id int primary key AUTO_INCREMENT,name VARCHAR(40))")

insertion = "INSERT INTO my_table2(id,name)VALUES(%s,%s)"

data = [(101,"KyawKyaw"),(102,"MgMg"),(103,"AungAung"),(104,"ZawZaw")]

#my_cursor.executemany(insertion,data)

#my_db.commit()

my_cursor.execute("UPDATE my_table2 SET name = 'Phonne' WHERE id = 101 ")

my_db.commit()

my_cursor.execute("DELETE FROM my_table2 WHERE id = 103")

my_db.commit()

my_cursor.execute("SELECT id,name FROM my_table2 ORDER BY name ")

all_data = my_cursor.fetchall()

for db in all_data:
  print(db)
