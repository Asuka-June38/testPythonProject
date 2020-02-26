# conn = pyodbc.connect("Driver = {SQL Server Native Client 11.0};"
#                       "Server = Adventure Works;"
#                       "Database = AdventureWorks2012;"
#                       "username = Sample User;"
#                       "password = User_Password;"
#                       "Trusted_Connection = yes;")


import pymssql

host = "40.68.37.158:1433"
username = "Sample user"
password = "rootroot"
database = "Adventure works"

conn = pymssql.connect(host, username, password, database)
cursor = conn.cursor()
cursor.execute('SELECT ProductName FROM Northwind.Products WHERE ProductID = 1;')

cursor.close()
conn.close()
