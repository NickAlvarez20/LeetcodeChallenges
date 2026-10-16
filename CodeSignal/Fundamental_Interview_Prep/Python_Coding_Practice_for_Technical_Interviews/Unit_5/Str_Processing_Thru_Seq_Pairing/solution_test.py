import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution('BCAAB'), ['B', 'A', 'A', 'B', 'C'])

    def test_case_2(self):
        self.assertEqual(solution('AB'), ['A', 'B'])

    def test_case_3(self):
        self.assertEqual(solution('A'), ['A'])

    def test_case_4(self):
        self.assertEqual(solution('CBA'), ['B', 'A', 'C'])

    def test_case_5(self):
        self.assertEqual(solution('AAA'), ['A', 'A', 'A'])

    def test_case_6(self):
        self.assertEqual(solution('XYZ'), ['X', 'Y', 'Z'])

    def test_case_7(self):
        self.assertEqual(solution('ABCDE'), ['A', 'C', 'B', 'D', 'E'])

if __name__ == '__main__':
    unittest.main()