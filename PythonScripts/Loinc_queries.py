import pyodbc 

# DB Connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS\GME468;'
                      'Database=GME468;'
                      'Trusted_Connection=yes;')

# Populate list with unique LabID for current date
cursor = conn.cursor()
cursor.execute('SELECT LabID FROM LoincTransactions WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE)')

unique_lab_list = []
for lab in cursor:
    if lab[0] not in unique_lab_list:
        unique_lab_list.append(lab[0])

cursor.close()

# Populate a list with Lab number and a list of tuples containing loinc number and loinc count
lab_info_list = []
for lab in unique_lab_list:
    lab = lab 
    lab_info_temp= []

    cursor = conn.cursor()
    cursor.execute(f'SELECT TOP 3 LoincID, COUNT(*) as LoincCount FROM LoincTransactions WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE) AND LabID = {lab} GROUP BY LoincID ORDER BY LoincCount DESC')

    loinc_count = cursor.fetchall()

    lab_info_temp.append(lab)
    lab_info_temp.append(loinc_count)
    lab_info_list.append(lab_info_temp)

    cursor.close()
