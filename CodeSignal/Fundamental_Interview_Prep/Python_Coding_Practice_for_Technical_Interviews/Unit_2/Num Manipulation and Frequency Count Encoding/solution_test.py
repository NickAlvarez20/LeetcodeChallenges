import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input_data = [1, 2, 3, 4, 5]
        expected_output = [2, 3, 4, 5, 6]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_2(self):
        input_data = [10, 20, 30, 40, 50]
        expected_output = [5]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_3(self):
        input_data = [10]
        expected_output = [1]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_4(self):
        input_data = [-10, 0, 10]
        expected_output = [3]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_5(self):
        input_data = [-1, 0, 1]
        expected_output = [0, 1, 2]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_6(self):
        input_data = [-100, -50, 0, 50, 100]
        expected_output = [5]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_7(self):
        input_data = [4, 13, -15, 20, 100, -10, -99, 98]
        expected_output = [-98, -14, 3, 5, 14, 99]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_8(self):
        input_data = [10, -20, 30, -40, -50, 60, 70, 80, 90, 100]
        expected_output = [10]
        self.assertEqual(solution(input_data), expected_output)

    def test_case_9(self):
        input_data = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]
        expected_output = [10]
        self.assertEqual(solution(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()