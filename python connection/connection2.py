from itertools import count
import psycopg2
from psycopg2 import Error





connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="databasedb")

# Create a cursor to perform database operations
cursor = connection.cursor()
#cursor.execute('drop table if exists person')
create_script ='''Create table accounting2(
                 id   int,
                 account_number int,
                 name varchar(40) not null,
                 balance int,
                 lasttransction varchar(40)
                 )'''

#cursor.execute(create_script)
insert_script ='insert into accounting2 (id,account_number,name,balance,lasttransaction) values (%s,%s,%s,%s,%s)'
insert_value=(1,123,'jhoncarpenter',1000,'null')
cursor.execute(insert_script,insert_value)

connection.commit()

cursor.close()
connection.close()