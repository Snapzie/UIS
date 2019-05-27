from prototype import conn, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Patients
    WHERE CPR_number = %s
    """
    cur.execute(sql, (int(user_id),))
    if cur.rowcount > 0:
        return Patients(cur.fetchone())
    else:
        return None

class Patients(tuple, UserMixin):
    def __init__(self, user_data):
        self.CPR_number = user_data[0]
        self.password = user_data[1]

    def get_id(self):
       return self.CPR_number

class Prescription(tuple):
    def __init__(self, user_data):
        self.pharmacy_name = user_data[0]
        self.medicine_name = user_data[1]
        self.medicine_concentration = user_data[2]
        self.patient_CPR = user_data[3]
        self.renewal = user_data[4]
        self.status = user_data[5]
        self.prescribed = user_data[6]
        self.expiration = user_data[7]
        self.illness = user_data[8]
        self.active = user_data[9]

class History(tuple):
    def __init__(self, user_data):
        self.medicine_name = user_data[0]
        self.medicine_concentration = user_data[1]
        self.renewal = user_data[2]
        self.illness = user_data[3]

class In_treatment_for(tuple):
    def __init__(self, user_data):
        self.patient_CPR = user_data[0]
        self.illness = user_data[1]

def select_Patient(CPR_number, conn):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Patients
    WHERE CPR_number = %s
    """
    cur.execute(sql, (CPR_number,))
    user = Patients(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user

def get_Prescriptions(CPR_number, conn):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Prescription
    WHERE patient_CPR = %s
    """
    cur.execute(sql, (CPR_number,))
    prescriptions = []
    for row in cur.fetchall():
        prescriptions.append(Prescription(row))
    cur.close()
    return prescriptions

def get_Active_Prescriptions(CPR_number, conn):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Prescription
    WHERE patient_CPR = %s
    AND active = 'Active'
    """
    cur.execute(sql, (CPR_number,))
    prescriptions = []
    for row in cur.fetchall():
        prescriptions.append(Prescription(row))
    cur.close()
    return prescriptions

def get_History(CPR_number, conn):
    p = get_Prescriptions(CPR_number, conn)
    history = []
    for perc in p:
        history.append(History((perc.medicine_name, perc.medicine_concentration, perc.renewal, perc.illness)))
    return history

def get_Diagnoses(CPR_number, conn):
    cur = conn.cursor()
    sql = """
        SELECT * FROM In_treatment_for
        WHERE patient_CPR = %s
        """
    cur.execute(sql, (CPR_number,))
    diagnoses = []
    for row in cur.fetchall():
        diagnoses.append(In_treatment_for(row))
    cur.close()
    return diagnoses

def update_Active_Prescription(CPR_number, med_name, med_conc, conn):
    cur = conn.cursor()
    sql = """
        UPDATE Prescription
        SET active = 'Inactive'
        WHERE medicine_name = %s AND medicine_concentration = %s AND patient_CPR = %s
    """
    cur.execute(sql, (med_name, med_conc, CPR_number))
    #cur.commit()
    cur.close()

# ======= Describe hard coded values in report =======
def insert_New_Renewed_Prescription(CPR_number, med_name, med_conc, conn):
    update_Active_Prescription(CPR_number, med_name, med_conc, conn)
    cur = conn.cursor()
    sql = """
        INSERT INTO Prescription(pharmacy_name, medicine_name, medicine_concentration, patient_CPR, renewal, status, prescribed, expiration, illness, active)
        VALUES('Pharmacy 1', %s, %s, %s, current_date, 'Ordered', current_date, current_date, 'Diabetes', 'Active')
    """
    cur.execute(sql, (med_name, med_conc, CPR_number))
    #cur.commit()
    cur.close()