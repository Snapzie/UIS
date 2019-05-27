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
    name text,
    concentration text,
    PRIMARY KEY (name, concentration)
);

CREATE TABLE IF NOT EXISTS Prescription(
    pharmacy_name text REFERENCES Pharmacy(name),
    medicine_name text,
    medicine_concentration text,
    patient_CPR integer REFERENCES Patients(CPR_number),
    renewal date,
    status text,
    prescribed date,
    expiration date,
    illness text REFERENCES Diagnose(illness),
    active text,
    FOREIGN KEY (medicine_name, medicine_concentration) REFERENCES Medicine(name, concentration),
    PRIMARY KEY (medicine_name, medicine_concentration, patient_CPR, renewal)
);

CREATE TABLE IF NOT EXISTS In_treatment_for(
    patient_CPR integer REFERENCES Patients(CPR_number),
    illness text REFERENCES Diagnose(illness),
    PRIMARY KEY (patient_CPR, illness)
);
