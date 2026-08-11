import unittest
from solution import solution


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution([1, 2, 3, 2, -3, 5, 2, 7, -1, 4]), [1, 2, 4, 4, -1, 8, 8, 8, -1, 4]
        )

    def test_case_2(self):
        self.assertEqual(
            solution([3, 4, -1, 2, 5, -2, 1, 5, 6]), [2, 2, -1, 5, 5, -1, 1, 5, 6]
        )

    def test_case_3(self):
        self.assertEqual(solution([-1, 2, 3, 4, 5]), [-1, 2, 3, 4, 5])

    def test_case_4(self):
        self.assertEqual(solution([5, 4, 3, 2, 1, -1]), [5, 5, 5, 5, 5, -1])

    def test_case_5(self):
        self.assertEqual(solution([7, 6, 5, 4, -1, 2, 1]), [4, 4, 4, 4, -1, 2, 1])

    def test_case_6(self):
        self.assertEqual(solution([1, 1, 1, 1, 1, 1, -1]), [1, 1, 1, 1, 1, 6, -1])

    def test_case_7(self):
        self.assertEqual(
            solution([-2, 3, 2, -4, 5, 1, -1, 2]), [-1, 3, 3, -1, 6, 6, -1, 2]
        )


if __name__ == "__main__":
    unittest.main()
