-- Patients
INSERT INTO public.Patients(CPR_number, password) VALUES (5000, 'Hej');
INSERT INTO public.Patients(CPR_number, password) VALUES (1000, 'Hej');
-- Diagnose
INSERT INTO public.Diagnose(illness) VALUES ('Diabetes');
-- Pharmacy
INSERT INTO public.Pharmacy(name, address) VALUES ('Pharmacy 1', 'Street 1');
INSERT INTO public.Pharmacy(name, address) VALUES ('Pharmacy 2', 'Street 2');
-- Medicine
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 1', '1M');
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 2', '2M');
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 3', '3M');
-- Prescription
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration) VALUES ('Pharmacy 1', 'Medicine 1', '1M', 5000, current_date, 'Ordered', current_date, current_date);
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration) VALUES ('Pharmacy 1', 'Medicine 2', '2M', 5000, TO_DATE('17/12/2015', 'DD/MM/YYYY'), 'Ordered', current_date, current_date);
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration) VALUES ('Pharmacy 1', 'Medicine 3', '3M', 5000, TO_DATE('17/12/2016', 'DD/MM/YYYY'), 'Ordered', current_date, current_date);
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration) VALUES ('Pharmacy 2', 'Medicine 1', '1M', 1000, TO_DATE('17/12/2017', 'DD/MM/YYYY'), 'Ordered', current_date, current_date);
