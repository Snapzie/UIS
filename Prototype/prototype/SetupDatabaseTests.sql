DROP TABLE IF EXISTS Patients CASCADE;
CREATE TABLE IF NOT EXISTS Patients(
    CPR_number integer PRIMARY KEY,
    password varchar(120)
);
INSERT INTO public.Patients(CPR_number, password) VALUES (5000, 'abe');
commit;