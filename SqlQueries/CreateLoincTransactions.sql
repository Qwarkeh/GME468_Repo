USE GME468

DROP TABLE LoincTransactions

CREATE TABLE LoincTransactions (
TransID int IDENTITY (1,1) NOT NULL PRIMARY KEY,
TransDate DATETIME NOT NULL,
LoincID INT NOT NULL FOREIGN KEY REFERENCES LOINC_Primary(IDCol),
LabID INT NOT NULL FOREIGN KEY REFERENCES Laboratories(LabID),
LabResultDate DATETIME,
IsPositive BIT, --if lab test returns positive return 1; if negative return 0
icd10cm nvarchar(255), --to be filled out if test returns positive
CptCode nvarchar(255)
);

--FIRST LAB--
INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2) -- LOINCs are not unique, and specific versions are being referenced with the auto-incremented identity key in the LOINC_Primary table

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 2)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 2)

--SECOND LAB--
INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 12)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 12)

--THIRD LAB--
INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 383491, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 158622, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 29)

INSERT INTO LoincTransactions (TransDate, LoincID, LabID)
VALUES (GETDATE(), 81791, 29)
