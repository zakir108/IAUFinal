import pyodbc # which library did u use for database connection
import matplotlib.pyplot as pt
import numpy as np
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=ALBATROSS\\SQLEXPRESS;"
                      "Database=W3School;"
                      "Trusted_Connection=yes;")

myDBCommand = cnxn.cursor()
myDBCommand.execute('SELECT * FROM products')

arr = []
for myRow in myDBCommand:   
    Pname = myRow[1] 
    arr.append(Pname)
    
print(arr)    
