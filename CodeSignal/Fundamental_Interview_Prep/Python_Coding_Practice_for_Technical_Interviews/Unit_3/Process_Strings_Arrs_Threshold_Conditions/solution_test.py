import unittest
from solution import solution


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        array = [5, 10, 15, 20, 25]
        string = "hello world"
        expected_output = ("ifm", [20, 25])
        self.assertEqual(solution(array, string), expected_output)

    def test_case_2(self):
        array = [-5, -10, -15, -20, -25]
        string = "python is fun"
        expected_output = ("qz", [-15, -20, -25])
        self.assertEqual(solution(array, string), expected_output)

    def test_case_3(self):
        array = [10, 20, -10, -20, 30]
        string = "coding mastery"
        expected_output = ("dp", [-10, -20, 30])
        self.assertEqual(solution(array, string), expected_output)

    def test_case_4(self):
        array = [11, 23, 32, -65, -33]
        string = "buffalo buffalo buffalo"
        expected_output = ("cv", [32, -65, -33])
        self.assertEqual(solution(array, string), expected_output)

    def test_case_5(self):
        array = [40, -20, -10, -1, 1]
        string = "race car"
        expected_output = ("", [40, -20, -10, -1, 1])
        self.assertEqual(solution(array, string), expected_output)

    def test_case_6(self):
        array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        string = "the quick brown fox jumps over the lazy dog"
        expected_output = ("uif rv", [17, 19, 23, 29])
        self.assertEqual(solution(array, string), expected_output)

    def test_case_7(self):
        array = [100] * 20
        string = "longer string with all lowercase letters to test the condition when array sum exceeds threshold"
        expected_output = ("", [100] * 20)
        self.assertEqual(solution(array, string), expected_output)

    def test_case_8(self):
        array = [50, -25, 75, -80]
        string = "some mixed cases and even numbers!123"
        expected_output = ("", [50, -25, 75, -80])
        self.assertEqual(solution(array, string), expected_output)


if __name__ == "__main__":
    unittest.main()
