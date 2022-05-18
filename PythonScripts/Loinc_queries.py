import pyodbc
import arcpy 

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

# County loinc Count
county_list = ['Multnomah', 'Washington', 'Clackamas']
county_count_list = []
for county in county_list:
    cursor = conn.cursor()
    cursor.execute(f"SELECT TOP 3 LoincID, COUNT(*) AS LoincCount FROM LoincTransactions LEFT JOIN Laboratories ON LoincTransactions.LabID = Laboratories.LabID WHERE Laboratories.County = '{county}' GROUP BY LoincID ORDER BY LoincCount DESC")

    county_count = cursor.fetchall()

    county_temp = []
    county_temp.append(county)
    county_temp.append(county_count)
    county_count_list.append(county_temp)

    cursor.close()

# Update Pilot_Labs FC
fields = ['Loinc1', 'Loinc1Count', 'Loinc2', 'Loinc2Count', 'Loinc3', 'Loinc3Count', 'LabID']
fc = 'C:\Spring_2022\GME_468\ArcPro_Portion\OregonDiseasesMap_StarkC\OregonDiseases_StarkC.gdb\Pilot_Labs'

with arcpy.da.UpdateCursor(fc, fields, sql_clause = (None, 'ORDER BY LabID')) as cursor:
    for row in cursor:
        for lab in lab_info_list:
            labID = lab[0]

            if labID == row[6]:
                print(f'Updating Lab {lab[0]}')
                #Loinc 1
                row[0] = lab[1][0][0] 
                row[1] = lab[1][0][1]
                #Loinc 2
                row[2] = lab[1][1][0]
                row[3] = lab[1][1][1]
                #loinc 3
                row[4] = lab[1][2][0]
                row[5] = lab[1][2][1]
                cursor.updateRow(row)
            else:
                continue
del cursor, row