import numpy as np
import pandas as pd
dict1 = {
    "name":['harry','rohan','raju','kalyan'],
    "marks":[92,34,54,45],
    "city":['rampur','kolkata','hyderabad','telangana']
}
df = pd.DataFrame(dict1)
print(df)

#df.to_csv('friend.csv')
#s=df.head(2)
#s=df.tail(1)
#s=df.describe()
#train=pd.read_csv('train.csv')
#print(train)
#vehicle=pd.read_csv('vehicle.csv')
accounting=pd.read_csv('accounting.csv')
print(accounting)