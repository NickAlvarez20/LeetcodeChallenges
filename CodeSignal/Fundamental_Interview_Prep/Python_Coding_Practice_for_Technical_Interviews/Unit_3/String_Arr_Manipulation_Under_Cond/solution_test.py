import unittest
from solution import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        input_string = "example"
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = ("iyenqmi", [8, 9, 10])
        self.assertEqual(solution(input_string, array), expected_output)

    def test2(self):
        input_string = "programming"
        array = [10, 10, 10, 10, 10, 10]
        expected_output = ("qsuh", [10, 10])
        self.assertEqual(solution(input_string, array), expected_output)

    def test3(self):
        input_string = "abc"
        array = [10, 20, 30, 40, 50]
        expected_output = ("ecd", [40, 50])
        self.assertEqual(solution(input_string, array), expected_output)

    def test4(self):
        input_string = "abcdefghijk"
        array = [5, 10]
        expected_output = ("ec", [])
        self.assertEqual(solution(input_string, array), expected_output)

    def test5(self):
        input_string = "negative"
        array = [-1, -2, -3, -4, -5, -6, -7, -8]
        expected_output = ("pihevowi", [])
        self.assertEqual(solution(input_string, array), expected_output)

    def test6(self):
        input_string = "zero"
        array = [0, 0, 0]
        expected_output = ("bis", [])
        self.assertEqual(solution(input_string, array), expected_output)

    def test7(self):
        input_string = "a"
        array = [100]
        expected_output = ("e", [])
        self.assertEqual(solution(input_string, array), expected_output)

    def test8(self):
        input_string = ""
        array = []
        expected_output = ("", [])
        self.assertEqual(solution(input_string, array), expected_output)

    def test9(self):
        input_string = "a" * 100
        array = [1] * 100
        expected_output = ("e" * 34, [1] * 66)
        self.assertEqual(solution(input_string, array), expected_output)


if __name__ == "__main__":
    unittest.main()
