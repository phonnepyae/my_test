import pymysql

def connect_and_show_tables():
    try:
        # Connect to the database
        connection = pymysql.connect(
            host='localhost',          # Replace with your MySQL host
            user='root',      # Replace with your MySQL username
            password='toor',  # Replace with your MySQL password
            database='test_1',  # Replace with your database name
            charset='utf8mb4',         # Optional: Ensure proper character encoding
            cursorclass=pymysql.cursors.DictCursor  # Use DictCursor for row-to-dict mapping
        )
        
        print("Connected to MySQL database")
        
        # Create a cursor to interact with the database
        with connection.cursor() as cursor:
            # Execute the query to show tables
            cursor.execute("SHOW TABLES")
            
            # Fetch all results
            tables = cursor.fetchall()
            
            if tables:
                print("Tables in the database:")
                for table in tables:
                    print(list(table.values())[0])  # Extract table name from the dictionary
            else:
                print("No tables found in the database.")
                
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()
            print("MySQL connection closed.")

# Call the function
connect_and_show_tables()