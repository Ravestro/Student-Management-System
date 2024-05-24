# Connecting to database

def database_connect():
    connection = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Raveen123$',
                database = 'Student Management System'
            )
    cursor = connection.cursor()
    print("\n Connected to database")
    return connection,cursor