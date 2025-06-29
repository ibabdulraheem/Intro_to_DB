import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Phoenix1982@..."
)
mycursor = mydb.cursor()
myresult = mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print(myresult)
mydb.commit()
if True:
  print ("Database 'alx_book_store' created successfully!")
raise mysql.connector.errors.DatabaseError ("Database already exist")


    
   




 
  