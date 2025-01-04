import pymysql


my_db = pymysql.connect(
  host="b1aiyspuicsgeab2zwts-mysql.services.clever-cloud.com",
  user="ublfdzv34ovb3kkx",
  passwd="pd4DkbHomP0ffsYhGPOe",
  database="b1aiyspuicsgeab2zwts"
  
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE TABLE cloud_db(roll_number int primary key AUTO_INCREMENT,name VARCHAR(40),age SMALLINT)")



my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
  print(db)