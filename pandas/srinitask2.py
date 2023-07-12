import numpy as np
import pandas as pd
from itertools import count
import psycopg2
from psycopg2 import Error
import xlrd


connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="databasedb")
cursor=connection.cursor()

create_script ='''Create table account(
                 Id   int,
                 Account_number int,
                 Name varchar(40) not null,
                 Balance int,
                 Last_transction varchar(40)
                 )'''

#cursor.execute(create_script)

location =("C:\\Users\\ThanniruAnkamraju\\Documents\\account.xlsx")
a =xlrd.open_workbook(location)
sheet = a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,3):
    print(tuple(sheet.row_values(i)))
    

connection.commit()

cursor.close()
connection.close()