import unittest
from cosmo import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), [6, 6, 6])

    def test2(self):
        self.assertEqual(solution([-5, -8, -10, -22, -12]), [-17, -30, -20])

    def test3(self):
        self.assertEqual(solution([9, 98, -23, 4, -57]), [-48, 102, -46])

    def test4(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 10, 10, 10, 10])

    def test5(self):
        self.assertEqual(solution([0, 0, 0, 0, 0, 0]), [0, 0, 0])

    def test6(self):
        self.assertEqual(solution([100, -50, -20, 30, 100]), [200, -20, -40])

    def test7(self):
        self.assertEqual(
            solution([-200, 0, 200, -50, 50, 0, 200, -200]), [-400, 200, 200, 0]
        )

    def test8(self):
        self.assertEqual(solution([3, 5, 6, 7, 9, 20, -5, -4, -3]), [0, 1, 1, 27, 18])


if __name__ == "__main__":
    unittest.main()
