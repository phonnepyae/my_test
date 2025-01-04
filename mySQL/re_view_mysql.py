import pymysql


my_db = pymysql.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="mytest_db"
)


my_cursor = my_db.cursor()

