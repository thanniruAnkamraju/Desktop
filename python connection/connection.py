from itertools import count
import psycopg2
from psycopg2 import Error


def formate_spaces(*args, spaces=6) -> None:
    """
    Args:
        spaces (int, optional): _description_. Defaults to 6.

    Output:

        prints a string by taking interable

        Example:

            Something needs to be written here

    """
    s = "{:<spaces} ".replace("spaces", str(spaces))*len(args[0])

    print(s.format(*args[0]))


connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="Rajudb")

# Create a cursor to perform database operations
cursor = connection.cursor()
#cursor.execute('drop table if exists person')
create_script ='''Create table person2(
                 id   serial primary key ,
                 name varchar(40) not null,
                 salary int
                 )'''

#cursor.execute(create_script)
insert_script ='insert into person2 (name,salary) values (%s,%s)'
insert_value=(('ramesh',1000),('ganesh',3000),('sam',2000),('swam',5000))
for record in insert_value:
   print(record)
#    cursor.execute(insert_script,record)
  # update_script='update person2 set salary = salary +(salary * 0.5)'
   #cursor.execute(update_script)
   
#    delete_script='delete from  person2  where name =%s'
#    delete_record =('swam',)
#    cursor.execute(delete_script,delete_record)
    # connection.commit()
   # print('end')
    
    #cursor.execute('select * from person')
   # for record in cursor.fetchall():
      #  print(record)
    #
#cursor.executemany(insert_script,insert_value)
connection.commit()

    


# for i in cursor.fetchall():
#     # print("{:<3} {:<20} {:<15} {:<12}".format(*map(str, i)))
#      formate_spaces(list(map(str, i)), spaces=14)
#     #print(i)


cursor.close()
connection.close()