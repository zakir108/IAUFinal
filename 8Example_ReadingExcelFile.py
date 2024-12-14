
import pandas as pd
from ExampleClasData import TestData


#dataframe
df = pd.read_excel("C://xl//file.xlsx", index_col=None, na_values=['NA'], usecols="B,C,D,E,F")


thislist = []

#Reading an Excel FIle
for index, row in df.iterrows():   # index =0, 1, 2,.....
    firtname =  row[0] #reading column1 Data
    lastname = row[1]  #reading column2 Data
    email =   row[2]   #reading column3 Data    
    phone = row[3]     #if you read 3 columnd remove this line
    address = row[4]   #if you read 3 columnd remove this line    
    data1 = TestData(row[0],row[1],row[2],row[3],row[4])
    thislist.append(data1)
 
print(thislist)