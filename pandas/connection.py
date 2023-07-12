from itertools import count
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="connectiondb")
# creating cursor to perform database operations
cursor=connection.cursor()
create_script='''create table employee(
              id serial primary key,
              name varchar(40),
              salary int
)'''
#cursor.execute(create_script)
insert_script ='insert into employee(name,salary) values(%s,%s)'
insert_value = (('ramesh',10000),('ganesh',20000),('swathi',3000),('raju',4000))
#cursor.executemany(insert_script,insert_value)

### update script##
update_script  = 'update employee set salary = (salary-100) where id = 2;'
#update_script = 'update empolyee set salary = (salary+100) where id = 2;'
#cursor.execute(update_script)
delete_script = 'delete from employee where id = 4;'
cursor.execute(delete_script)
connection.commit()
connection.close()