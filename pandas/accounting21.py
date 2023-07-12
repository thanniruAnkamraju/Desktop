import numpy as np
import pandas as pd
import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="databasedb")
cursor = connection.cursor()
df=pd.read_excel('C:\\Users\\ThanniruAnkamraju\\Desktop\\pandas\\accounting21.xlsx') 

df['Total_amount']=df['Balance']-df['Balance']*(10/100)
print(df['Total_amount'])
cursor.execute('drop table if exists accounting21')
sql="""CREATE TABLE accounting21 (Id INTEGER,Account_number INTEGER,Name VARCHAR(50),Balance FLOAT,Deduct  VARCHAR(100),Total_amount FLOAT)"""
cursor.execute(sql)
#Transfer Dataframe to postgress
insert_query="""INSERT INTO accounting21 (Id,Account_number,Name,Balance,Deduct,Total_amount) VALUES (%s,%s,%s,%s,%s,%s)"""
for r in df.values:
    cursor.execute(insert_query,r.tolist())
connection.commit()
connection.close()