import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=localhost\SQLEXPRESS;'
                            'Database=BP;'
                            'Trusted_Connection=yes;')

cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.columns")

for row in cursor:
    print(row)