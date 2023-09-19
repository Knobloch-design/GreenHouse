import mysql.connector  # import the MySQL connector library

mydb = mysql.connector.connect(
  host="alectestdb.cb4kadb1h8mb.us-east-2.rds.amazonaws.com",
  user="alecmaliky",
  password="markisthegoat"
)
print("Connected")
mycursor = mydb.cursor()  # create a cursor object to interact with the database

# create a new database
mycursor.execute("CREATE DATABASE temperature")
mycursor.execute("CREATE TABLE temperature (Id INTEGER PRIMARY KEY, temp_c REAL);")
mycursor.commit()
