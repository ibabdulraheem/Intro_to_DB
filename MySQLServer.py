import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Phoenix1982@..."
)
mycursor = mydb.cursor()
myresult = mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print(myresult)
try:
  mydb.commit()
  print("Database 'alx_book_store' created successfully! ")
except mysql.connector.Error:
    print("Database already exist")


    
   




 
  