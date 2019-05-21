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
    return prescriptions