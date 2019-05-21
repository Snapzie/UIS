DELETE FROM Patients;
DELETE FROM Diagnose;
DELETE FROM Pharmacy;
DELETE FROM Medicine;
DELETE FROM Prescription;
DELETE FROM History;
DELETE FROM In_treatment_for;

-- Patients
INSERT INTO public.Patients(CPR_number, password) VALUES (5000, 'Hej');
-- Diagnose
INSERT INTO public.Diagnose(illness) VALUES ('Diabetes');
-- Pharmacy
INSERT INTO public.Pharmacy(name, address) VALUES ('Pharmacy 1', 'Street 1');
-- Medicine
INSERT INTO public.Medicine(name, concentration) VALUES ('Medicine 1', '2M');
-- Prescription
INSERT INTO public.Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration) VALUES ('Pharmacy 1', 'Insulin', '2M', 5000, current_date, 'Ordered', current_date, current_date);
