from datetime import datetime
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
       return (self.CPR_number)

class Diagnose(tuple):
    def __init__(self, user_data):
        self.illness = user_data[0]

class Pharmacy(tuple):
    def __init__(self, user_data):
        self.name = user_data[0]
        self.address = user_data[1]

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

class History(tuple):
    def __init__(self, user_data):
        self.patient_CPR = user_data[0]
        self.medicine_name = user_data[1]
        self.medicine_concentration = user_data[2]
        self.diagnosed_illness = user_data[3]
        self.time = user_data[4]

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
    user = Patients(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user

def select_Prescriptions(CPR_number, conn):
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

def insert_History(prescription, conn):
    cur = conn.cursor()
    sql = """
    INSERT INTO History(patient_CPR, medicine_name, medicine_concentration, diagnosed_illness, time) 
    VALUES (%s, %s, %s, %s, CURRENT_DATE)
    """
    cur.execute(sql, (prescription.patient_CPR, prescription.medicine_name, prescription.medicine_concentration, prescription.illness))
    cur.close()

def get_History(CPR_number, conn):
    cur = conn.cursor()
    sql = """
    SELECT * from History WHERE patient_CPR = %s
    """
    cur.execute(sql,(CPR_number,))
    history = []
    for row in cur.fetchall():
        history.append(History(row))
    cur.close()
    return history