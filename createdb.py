import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Root@123'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mysqldb")

print("All Done")

