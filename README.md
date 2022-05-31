# GME468_Repo
GME468_Repo hosts a python script that pulls data from a local SQL Server database and uses it to update feature classes with the ArcGIS API for python. It then overwrites the applicable existing layers on ArcGIS Online.

# Script Name
dashboard_update.py 

# Mandatory User alterations
The code was originally written to work on only one specific machine with a set of private ArcGIS login credentials."

Lines 7 to 11 must be altered for the SQL Server database connection.
Lines 120 and 121 hold the login information.
