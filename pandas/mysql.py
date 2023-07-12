
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Raju@12345",
  database="sys"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers2 (name VARCHAR(255), address VARCHAR(255))")