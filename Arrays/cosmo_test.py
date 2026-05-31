import unittest
from math import sqrt

from cosmo import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solution([1, 2, 3, 4, 5]),
            [(1, 2.24), (2, 2.83), (3, 3.0), (4, 2.83), (5, 2.24)],
        )

    def test2(self):
        self.assertEqual(
            solution([3, 2, 1, 0, 1, 2, 3]),
            [(3, 3.0), (2, 2.0), (1, 1.0), (0, 0.0), (1, 1.0), (2, 2.0), (3, 3.0)],
        )

    def test3(self):
        self.assertEqual(solution([100, 100]), [(100, 100.0), (100, 100.0)])

    def test4(self):
        self.assertEqual(
            solution([12, 45, 67, 34, 89, 56]),
            [
                (12, 25.92),
                (45, 63.29),
                (67, 47.73),
                (34, 47.73),
                (89, 63.29),
                (56, 25.92),
            ],
        )

    def test5(self):
        self.assertEqual(
            solution([3, 2, 1, 0, 0, 1, 2, 3]),
            [
                (3, 3.0),
                (2, 2.0),
                (1, 1.0),
                (0, 0.0),
                (0, 0.0),
                (1, 1.0),
                (2, 2.0),
                (3, 3.0),
            ],
        )

    def test6(self):
        self.assertEqual(
            solution([0, 0, 0, 0, 0]),
            [(0, 0.0), (0, 0.0), (0, 0.0), (0, 0.0), (0, 0.0)],
        )

    def test7(self):
        self.assertEqual(solution([0]), [(0, 0.0)])

    def test8(self):
        self.assertEqual(solution([1]), [(1, 1.0)])


if __name__ == "__main__":
    unittest.main()
