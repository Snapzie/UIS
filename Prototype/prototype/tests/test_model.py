import unittest
from prototype.models import select_Patient, get_Prescriptions, get_History, get_Diagnoses
import psycopg2
import datetime

db = "dbname='prototypetests' user='Casper' host='localhost' password = ''"
conn = psycopg2.connect(db)
c = conn.cursor()


class MyTestCase(unittest.TestCase):
    def setUp(self):
        fd = open('/Users/Casper/Uni/UIS/UIS/Prototype/prototype/SetupDatabaseTests.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sqlCommands = filter(None, sqlFile.split(';'))

        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                c.execute(command)
            except Exception as inst:
                print("Command skipped: ", inst)

    def test_select_patient(self):
        u = select_Patient(5000, conn)
        self.assertTrue(u.password == 'abe' and u.CPR_number == 5000)

    def test_select_patient_none(self):
        u = select_Patient(0, conn)
        self.assertTrue(u is None)

    def test_get_prescriptions(self):
        p = get_Prescriptions(5000, conn)
        self.assertEqual(len(p), 3)

    def test_get_prescriptions_no_prescription(self):
        p = get_Prescriptions(2000, conn)
        self.assertEqual(len(p), 0)

    def test_get_diagnoses(self):
        d = get_Diagnoses(5000, conn)
        self.assertEqual(len(d), 1)

    def test_get_diagnoses_no_diagnoses(self):
        p = get_Prescriptions(2000, conn)
        self.assertEqual(len(p), 0)

    def test_select_prescriptions_is_class(self):
        p = get_Prescriptions(1000, conn)
        self.assertEqual(len(p), 1)
        perc = p[0]
        self.assertTrue(perc.patient_CPR == 1000 and perc.status == 'Ordered')

    def test_get_history(self):
        h = get_History(5000, conn)
        self.assertEqual(len(h), 3)
        self.assertTrue(h[0].name == 'Medicine 1')
        self.assertTrue(h[1].name == 'Medicine 2')
        self.assertTrue(h[2].name == 'Medicine 3')
        self.assertTrue(h[0].concentration == '1M')
        self.assertTrue(h[1].concentration == '2M')
        self.assertTrue(h[2].concentration == '2M')
        self.assertTrue(h[0].illness == 'Diabetes')
        self.assertTrue(h[1].illness == 'Diabetes')
        self.assertTrue(h[2].illness == 'Diabetes')
        self.assertTrue(str(h[0].renewal) == "2015-12-17")
        self.assertTrue(str(h[1].renewal) == "2016-12-17")
        self.assertTrue(str(h[2].renewal) == "2017-12-17")



if __name__ == '__main__':
    unittest.main()
