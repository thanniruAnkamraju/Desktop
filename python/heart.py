import numpy as np
import pandas as pd
import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Raju@123",
                              host="127.0.0.1",
                              port="5432",
                              database="connectiondb")
cur=connection.cursor()
df=pd.read_csv('C:\\Users\\ThanniruAnkamraju\\Downloads\\heart-disease.csv')
cur.execute('drop table if exists heart')
sql='''create table heart(age int,sex varchar(20),cp int,trestbps int,chol int,fbs int,restecg int,thalach int,exang int,oldpeak varchar(200),slope int,ca int,thal int,target int)'''
cur.execute(sql)
insert='''insert into heart (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

for r in df.values:
    cur.execute(insert,r.tolist())
connection.commit()
connection.close()