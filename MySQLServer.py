import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Phoenix1982@..."
)
mycursor = mydb.cursor()
myresult = mycursor.execute("CREATE DATABASE alx_book_store")
mydb.commit()