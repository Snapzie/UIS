-- Patients
INSERT INTO public.Patients(CPR_number, password) VALUES (1000, 'Hej');
INSERT INTO public.Patients(CPR_number, password) VALUES (2000, 'Hej');
INSERT INTO public.Patients(CPR_number, password) VALUES (5000, 'Hej');
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
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 3', '2M');
-- Prescription
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness, active) VALUES ('Pharmacy 1', 'Medicine 1', '1M', 5000, TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'Ready', current_date, current_date, 'Diabetes', 'Inactive');
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness, active) VALUES ('Pharmacy 1', 'Medicine 2', '2M', 5000, TO_DATE('17/12/2016', 'DD/MM/YYYY'), 'Approved', current_date, current_date, 'Diabetes', 'Active');
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness, active) VALUES ('Pharmacy 1', 'Medicine 3', '2M', 5000, TO_DATE('17/12/2017', 'DD/MM/YYYY'), 'Ready', current_date, current_date, 'Diabetes', 'Active');
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness, active) VALUES ('Pharmacy 2', 'Medicine 1', '1M', 1000, TO_DATE('17/12/2017', 'DD/MM/YYYY'), 'Approved', current_date, current_date, 'Diabetes', 'Active');