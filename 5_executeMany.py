import pymysql as Mysql


my_db = Mysql.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="mytest_db"
)

my_cursor = my_db.cursor()

#my_cursor.execute("CREATE TABLE my_table1(roll_number int primary key AUTO_INCREMENT,name VARCHAR(30),year VARCHAR(30),age SMALLINT)")


insert_data = "INSERT INTO my_table1(roll_number,name,year,age)values(%s,%s,%s,%s)"

data = [(1,"WAI YAN LING","Fouth Year",22),
        (2,"wai","fouth",23),
        (3,"yan","fouth",23)]

#my_cursor.executemany(insert_data,data)

my_db.commit()

print(my_cursor.rowcount)

my_cursor.execute("SELECT roll_number,name FROM my_table1 WHERE name LIKE 'wai'")
all_data = my_cursor.fetchall()
for db in all_data:
  print("%d-%s"%(db[0],db[1]))

