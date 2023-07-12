import numpy as np
import pandas as pd
import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="databasedb")
cursor = connection.cursor()
pf=pd.read_csv('C:\\Users\\ThanniruAnkamraju\\Desktop\\pandas\\accounting6.csv') 

pf['Last_transaction']=pf['Balance']-pf['Balance']*(10/100)
print(pf['Last_transaction'])
cursor.execute('drop table if exists accounting5')
sql="""CREATE TABLE accounting6 (Id INTEGER,Account_number INTEGER,Name VARCHAR(50),Balance FLOAT,Last_transaction FLOAT)"""
cursor.execute(sql)
#Transfer Dataframe to postgress
insert_query="""INSERT INTO accounting6 (Id,Account_number,Name,Balance,Last_transaction) VALUES (%s,%s,%s,%s,%s)"""
for r in pf.values:
        cursor.execute(insert_query,r.tolist())
connection.commit()
connection.close()
