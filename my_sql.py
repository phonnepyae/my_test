C:\Program Files\MySQL\MySQL Server 8.0\binC:\Program Files\MySQL\MySQL Server 8.0\bin
import mysql.connector

try:
    # Establishing the connection
    data_base_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="toor"
    )
    print("Connected to MySQL Server!")

    # Creating a cursor
    db_cursor = data_base_connection.cursor()

    # Creating a database (if it doesn't already exist)
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS testDB")

    # Showing all databases
    db_cursor.execute("SHOW DATABASES")

    print("Databases available:")
    for db in db_cursor:
        print(db[0])  # Print database name only

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if data_base_connection.is_connected():
        db_cursor.close()
        data_base_connection.close()
        print("MySQL connection closed.")

