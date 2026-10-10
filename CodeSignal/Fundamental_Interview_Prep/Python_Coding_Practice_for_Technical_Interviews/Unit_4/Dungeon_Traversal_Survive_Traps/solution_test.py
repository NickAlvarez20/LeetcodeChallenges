import unittest
from solution import solution

class TestSolution(unittest.TestCase): 
    def test_case_1(self):
        self.assertEqual(solution([0, -1, 1, 0, -1], 3), 1)

    def test_case_2(self):
        self.assertEqual(solution([1, 0, -1, 1, 0], 5), 2)

    def test_case_3(self):
        self.assertEqual(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10), 10)

    def test_case_4(self):
        self.assertEqual(solution([-3, -4, -2, -7, 8, -10, -3], 14), 1)

    def test_case_5(self):
        self.assertEqual(solution([1, 2, 3, 4, 5], 20), 5)

    def test_case_6(self):
        self.assertEqual(solution([100, 0, 0, 0, -10, 0, 0], 110), 1)

    def test_case_7(self):
        self.assertEqual(solution([0, -2, -4, -6, -8], 10), 1)


if __name__ == '__main__':
    unittest.main()