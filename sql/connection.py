import mysql.connector
import os

mydb=mysql.connector.connect(host='localhost',user='root',password='Raju@123',database='sys')
mycursor=mydb.cursor()

#mycursor.execute('create table customer(id int,name varchar(25),salary int)')

# insert into values #
sql = "INSERT INTO customer (id,name,salary) VALUES (%s,%s,%s)"
val =  (1,"Raju", 310000)
#mycursor.execute(sql, val)
##update
update_sql=("update customer set salary=salary+100 where id=3")
#mycursor.execute(update_sql)
##delete
delete_sql=("delete from customer where name=1")
mycursor.execute(delete_sql)
mydb.commit()
mycursor.close()




