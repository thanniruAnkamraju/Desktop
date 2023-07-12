import numpy as np
import pandas as pd
import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="connectiondb")
cursor = connection.cursor()
df=pd.read_excel('C:\\Users\\ThanniruAnkamraju\\Desktop\\pandas\\account1.xlsx') 

df['Last_transaction']=df['Balance']-df['Balance']*(10/100)
print(df['Last_transaction'])
df['Total_amount']=df['Balance']-df['Balance']*(90/100)
print(df['Total_amount'])
cursor.execute('drop table if exists account')
sql="""CREATE TABLE account1 (Id INTEGER,Account_number INTEGER,Name VARCHAR(50),Balance FLOAT,Deduct VARCHAR(200),Total_amount  VARCHAR(100),Last_transaction FLOAT)"""
cursor.execute(sql)
#Transfer Dataframe to postgress
insert_query="""INSERT INTO account1 (Id,Account_number,Name,Balance,Deduct,Total_amount,Last_transaction) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
for r in df.values:
    cursor.execute(insert_query,r.tolist())
connection.commit()
connection.close()