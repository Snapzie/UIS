DROP TABLE IF EXISTS Patients CASCADE;
DROP TABLE IF EXISTS Diagnose CASCADE;
DROP TABLE IF EXISTS Pharmacy CASCADE;
DROP TABLE IF EXISTS Medicine CASCADE;
DROP TABLE IF EXISTS Prescription CASCADE;
DROP TABLE IF EXISTS History CASCADE;
DROP TABLE IF EXISTS In_treatment_for CASCADE;

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
    expiration date,
    illness text REFERENCES Diagnose(illness)
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

-- Patients
INSERT INTO public.Patients(CPR_number, password) VALUES (1000, 'Hej');
INSERT INTO public.Patients(CPR_number, password) VALUES (2000, 'Hej');
INSERT INTO public.Patients(CPR_number, password) VALUES (5000, 'abe');
-- Diagnose
INSERT INTO public.Diagnose(illness) VALUES ('Diabetes');
-- In treatment for
INSERT INTO public.In_treatment_for(patient_CPR, illness) VALUES (1000, 'Diabetes');
INSERT INTO public.In_treatment_for(patient_CPR, illness) VALUES (5000, 'Diabetes');
-- Pharmacy
INSERT INTO public.Pharmacy(name, address) VALUES ('Pharmacy 1', 'Street 1');
INSERT INTO public.Pharmacy(name, address) VALUES ('Pharmacy 2', 'Street 2');
-- Medicine
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 1', '1M');
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 2', '2M');
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 3', '3M');
-- Prescription
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness) VALUES ('Pharmacy 1', 'Medicine 1', '1M', 5000, current_date, 'Ordered', current_date, current_date, 'Diabetes');
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness) VALUES ('Pharmacy 1', 'Medicine 2', '2M', 5000, TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'Ordered', current_date, current_date, 'Diabetes');
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness) VALUES ('Pharmacy 1', 'Medicine 3', '3M', 5000, TO_DATE('17/12/2016', 'DD/MM/YYYY'), 'Ordered', current_date, current_date, 'Diabetes');
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness) VALUES ('Pharmacy 2', 'Medicine 1', '1M', 1000, TO_DATE('17/12/2017', 'DD/MM/YYYY'), 'Ordered', current_date, current_date, 'Diabetes');
-- History
INSERT INTO public.History(patient_CPR, medicine_name, medicine_concentration, diagnosed_illness, time) VALUES (1000, 'Medicine 1', '1M','Diabetes',TO_DATE('17/12/2015', 'DD/MM/YYYY'));
commit;