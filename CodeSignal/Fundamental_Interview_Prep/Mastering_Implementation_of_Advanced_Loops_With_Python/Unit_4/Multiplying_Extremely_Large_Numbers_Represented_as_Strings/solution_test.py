import os
import sys
import unittest

# These line are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import solution


class SolutionTests(unittest.TestCase):
    def test01(self):
        self.assertEqual(solution("123456789", "987654321"), "121932631112635269")

    def test02(self):
        self.assertEqual(solution("123", "456"), "56088")

    def test03(self):
        self.assertEqual(solution("100", "200"), "20000")

    def test04(self):
        self.assertEqual(solution("500", "500"), "250000")

    def test05(self):
        self.assertEqual(solution("1000000000", "1000000000"), "1000000000000000000")

    def test06(self):
        self.assertEqual(solution("999999999", "1"), "999999999")

    def test07(self):
        self.assertEqual(solution("0", "500"), "0")

    def test08(self):
        self.assertEqual(solution("1", "1"), "1")

    def test09(self):
        self.assertEqual(solution("9", "9"), "81")

    def test10(self):
        self.assertEqual(solution("111111111", "111111111"), "12345678987654321")


if __name__ == "__main__":
    unittest.main()
