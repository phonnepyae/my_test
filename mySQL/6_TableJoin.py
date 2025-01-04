import pymysql


my_db = pymysql.connect(
  host="b1aiyspuicsgeab2zwts-mysql.services.clever-cloud.com",
  user="ublfdzv34ovb3kkx",
  passwd="pd4DkbHomP0ffsYhGPOe",
  database="b1aiyspuicsgeab2zwts"
  
)

my_cursor = my_db.cursor()

#my_cursor.execute("CREATE TABLE my_table3(id int primary key AUTO_INCREMENT,score SMALLINT,grade VARCHAR(10))")

insertion = "INSERT INTO my_table3(id,score,grade)VALUES(%s,%s,%s)"

data = [(101,600,"A"),(102,500,"A"),(104,500,"A")]

#my_cursor.executemany(insertion,data)

#my_db.commit()

my_cursor.execute("SELECT my_table2.id,my_table2.name,my_table3.score,my_table3.grade FROM my_table3 JOIN my_table2 ON my_table3.id = my_table2.id")

my_db.commit()

all_data = my_cursor.fetchall()

for db in all_data:
  print("%d %s %s %s"%(db[0],db[1],db[2],db[3]))