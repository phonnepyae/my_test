import pymysql as Mysql


my_db = Mysql.connect(
  
  host = "localhost",
  user = "root",
  passwd = "toor",
  database = "mytest_db" 
)

my_cursor = my_db.cursor()

#my_cursor.execute("CREATE TABLE my_table(roll_number int primary key AUTO_INCREMENT,name VARCHAR(40),year SMALLINT)")

#my_cursor.execute("ALTER TABLE my_table ADD age SMALLINT")

insert_datatype = "INSERT INTO my_table(roll_number,name,year,age)values(%s,%s,%s,%s)"

data_1 = (1,"WaiYanLing",4,22)


my_cursor.execute(insert_datatype,data_1)

my_db.commit()

print(my_cursor.rowcount)

my_cursor.execute("SELECT * FROM my_table")

for db in my_cursor:
  print(db)


#my_cursor.execute("DESCRIBE my_table")


#for db in my_cursor:
  #print(db)