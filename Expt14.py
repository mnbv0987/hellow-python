#Database operations in Python

# importing required libraries import mysql.connector
dataBase = mysql.connector.connect( host ="localhost",user ="root",passwd ="mysqlashish")

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE PYTHONDATABASE")
print("Database connection successful……")
database.close()


import mysql.connector
dataBase = mysql.connector.connect(host = "localhost", user = "root",passwd = "mysqlashish",database = "PYTHONDATABASE" )
cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE STUDENT (NAME VARCHAR(20) NOT NULL,
BRANCH VARCHAR(50), ROLL INT NOT NULL, SECTION VARCHAR(5), AGE INT)"""

# table created cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()


import mysql.connector
mydb = mysql.connector.connect( host = "localhost",
user = "root",
password = "mysqlashish", database = "pythondatabase")
mycursor = mydb.cursor()
sql = "INSERT INTO Student (Name,Branch,Roll,Section,Age) VALUES (%s, %s, %s, %s, %s)"
val = ("Ram", "IT", "12","A","20")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "details inserted")
mydb.close()

