import pyodbc 

# DB Connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS\GME468;'
                      'Database=GME468;'
                      'Trusted_Connection=yes;')

#
cursor = conn.cursor()
cursor.execute('SELECT * FROM Laboratories')

for i in cursor:
    print(i)

cursor.close()