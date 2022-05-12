USE GME468

--Grabs LOINC counts for today's date for the entire table

--Select LoincID, COUNT(*) AS LoincCount
--FROM LoincTransactions
--WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE)
--GROUP BY LoincID
--ORDER BY LoincCount DESC
---------------------------------------------------------------------

--Grabs overall LOINC count in the table

--Select LoincID, COUNT(*) AS LoincCount
--FROM LoincTransactions
--GROUP BY LoincID
--ORDER BY LoincCount DESC
---------------------------------------------------------------------

--Grabs LOINC counts for todays for each lab

--Select LoincID as "Lab2 LOINCs", COUNT(*) AS LoincCount
--FROM LoincTransactions
--WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE) AND LabID = 2
--GROUP BY LoincID
--ORDER BY LoincCount DESC

--Select LoincID as "Lab12 LOINCs", COUNT(*) AS LoincCount
--FROM LoincTransactions
--WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE) AND LabID = 12
--GROUP BY LoincID
--ORDER BY LoincCount DESC

--Select LoincID as "Lab29 LOINCs", COUNT(*) AS LoincCount
--FROM LoincTransactions
--WHERE CAST(TransDate as DATE) = CAST(GETDATE() as DATE) AND LabID = 29
--GROUP BY LoincID
--ORDER BY LoincCount DESC
----------------------------------------------------------------------

--LOINC counts by County

Select LoincID as "Multnomah LOINCs", COUNT(*) AS LoincCount
FROM LoincTransactions LEFT JOIN Laboratories
	ON LoincTransactions.LabID = Laboratories.LabID
WHERE Laboratories.County = 'Multnomah'
GROUP BY LoincID
ORDER BY LoincCount DESC

Select LoincID as "Washington LOINCs", COUNT(*) AS LoincCount
FROM LoincTransactions LEFT JOIN Laboratories
	ON LoincTransactions.LabID = Laboratories.LabID
WHERE Laboratories.County = 'Washington'
GROUP BY LoincID
ORDER BY LoincCount DESC

Select LoincID as "Clackamas LOINCs", COUNT(*) AS LoincCount
FROM LoincTransactions LEFT JOIN Laboratories
	ON LoincTransactions.LabID = Laboratories.LabID
WHERE Laboratories.County = 'Clackamas'
GROUP BY LoincID
ORDER BY LoincCount DESC