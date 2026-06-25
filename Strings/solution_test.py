import unittest
from solution import add_days

class TestFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(add_days('1999-01-01', 365), '2000-01-01')

    def test_case_2(self):
        self.assertEqual(add_days('2000-01-01', 365), '2000-12-31')

    def test_case_3(self):
        self.assertEqual(add_days('2000-01-01', 366), '2001-01-01')

    def test_case_4(self):
        self.assertEqual(add_days('2001-12-31', 1), '2002-01-01')

    def test_case_5(self):
        self.assertEqual(add_days('2000-12-31', 1), '2001-01-01')

    def test_case_6(self):
        self.assertEqual(add_days('2004-01-01', 1461), '2008-01-01')

    def test_case_7(self):
        self.assertEqual(add_days('1899-12-31', 50000), '2036-11-22')

    def test_case_8(self):
        self.assertEqual(add_days('2099-12-31', 50000), '2236-11-23')

if __name__ == '__main__':
    unittest.main()