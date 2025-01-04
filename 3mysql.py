import mysql.connector

my_db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd ="toor"
)

my_cursor = my_db.cursor()

my_cursor.execute("SHOW DATABASES")