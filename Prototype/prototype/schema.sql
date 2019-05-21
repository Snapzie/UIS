\i /Users/Casper/Uni/UIS/UIS/Prototype/prototype/schema_drop.sql

CREATE TABLE IF NOT EXISTS Patients(
    CPR_number integer PRIMARY KEY,
    password varchar(120)
);

CREATE TABLE IF NOT EXISTS Diagnose(
    illness text PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Pharmacy(
    name text PRIMARY KEY,
    address text
);

CREATE TABLE IF NOT EXISTS Medicine(
    name text PRIMARY KEY,
    concentration text UNIQUE
);

CREATE TABLE IF NOT EXISTS Prescription(
    pharmacy_name text REFERENCES Pharmacy(name),
    medicine_name text REFERENCES Medicine(name),
    medicine_concentration text REFERENCES Medicine(concentration),
    patient_CPR integer REFERENCES Patients(CPR_number),
    renewal date PRIMARY KEY,
    status text,
    prescribed date,
    expiration date
);

CREATE TABLE IF NOT EXISTS History(
    patient_CPR integer REFERENCES Patients(CPR_number),
    medicine_name text REFERENCES Medicine(name),
    medicine_concentration text REFERENCES Medicine(concentration),
    diagnosed_illness text REFERENCES Diagnose(illness),
    time date default current_date PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS In_treatment_for(
    patient_CPR integer REFERENCES Patients(CPR_number),
    illness text REFERENCES Diagnose(illness)
);
