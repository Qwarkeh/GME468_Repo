from doctest import master
from numpy import append
from collections import Counter
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

# List of dictionaries that hold each lab's loinc information
master_lab_list= []
for lab in unique_lab_list:
    labID = lab 
    loinc_list = []
    lab_dict = {}
    lab_import_list = []

    lab_dict[f'LabID'] = f'{labID}'

    cursor = conn.cursor()
    cursor.execute(f'SELECT LoincID FROM LoincTransactions WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE) AND LabID = {labID}')

    for value in cursor:
        loinc_list.append(value[0])

    loinc_count = Counter(loinc_list).items()

    counter = 1
    for loinc in loinc_count:
        lab_dict[f'loinc{counter}'] = f'{loinc[0]}'
        lab_dict[f'loinc{counter}_count'] = f'{loinc[1]}'

        counter += 1

    cursor.close()
    print(lab_dict)

for dict in master_lab_list:
    print(dict)   
