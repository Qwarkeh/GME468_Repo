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

# For each labID in unique_lab_list
# Create a dictionary for each lab that stores: loinc1, loinc1_count, loinc2, loinc2_count, loinc3_loinc3_count
# Append dictionary to unique_lab_list

#for lab in unique_lab_list:

labID = '2'
loinc_list = []
lab2_dict = {}

cursor = conn.cursor()
cursor.execute(f'SELECT LoincID FROM LoincTransactions WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE) AND LabID = {labID}')

""" for value in cursor:
    if value[0] not in loinc_list:
        loinc_list.append(value[0]) """

for value in cursor:
    loinc_list.append(value[0])

loinc_count = Counter(loinc_list).items()

counter = 1
for loinc in loinc_count:
    loinc_number = lab2_dict[f'loinc{counter}'] = f'{loinc[0]}'
    loinc_count = lab2_dict[f'loinc{counter}_count'] = f'{loinc[1]}'

    print(loinc_number)
    print(loinc_count)

    counter += 1

print(lab2_dict)

cursor.close()
