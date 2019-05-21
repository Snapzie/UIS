import unittest
from prototype.models import select_Patient, select_Prescriptions
import psycopg2

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

    def test_select_prescriptions(self):
        p = select_Prescriptions(5000, conn)
        self.assertEqual(len(p), 3)

    def test_select_prescriptions_no_prescription(self):
        p = select_Prescriptions(2000, conn)
        self.assertEqual(len(p), 0)

    def test_select_prescriptions_is_class(self):
        p = select_Prescriptions(1000, conn)
        self.assertEqual(len(p), 1)
        perc = p[0]
        self.assertTrue(perc.patient_CPR == 1000 and perc.status == 'Ordered')


if __name__ == '__main__':
    unittest.main()
