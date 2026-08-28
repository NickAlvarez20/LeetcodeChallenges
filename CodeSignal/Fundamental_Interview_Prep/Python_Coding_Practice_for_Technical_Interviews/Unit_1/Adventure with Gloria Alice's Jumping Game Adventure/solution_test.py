import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arrayA = [1, 3, 2, 5, 4]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [1, 4, 3, 2, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_2(self):
        arrayA = [1, 1, 1, 1, 1]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_3(self):
        arrayA = [2, 3, 4, 5, 1]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [2, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_4(self):
        arrayA = [1, 5, 2, 4, 3]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_5(self):
        arrayA = [4, 3, 2, 1, 5]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [4, 3, 2, 1, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_6(self):
        arrayA = [5, 4, 3, 2, 1]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [5, 1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_7(self):
        arrayA = [5, 1, 2, 3, 4]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_8(self):
        arrayA = [1, 2, 3, 4, 5]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_9(self):
        arrayA = [3, 2, 1, 5, 4]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [3, 1, 4, 2, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_10(self):
        arrayA = [2, 3, 4, 1, 5]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [2, 3, 4, 1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)


if __name__ == "__main__":
    unittest.main()
