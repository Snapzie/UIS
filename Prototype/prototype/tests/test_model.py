import unittest
from prototype import models


class MyTestCase(unittest.TestCase):
    def test_select_patient(self):
        u = models.select_Patient(5000)
        self.assertTrue(u.password == 'Hej')


if __name__ == '__main__':
    unittest.main()
