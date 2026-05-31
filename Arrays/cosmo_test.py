import unittest
from cosmo import solution


class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(43172), 21)

    def test2(self):
        self.assertEqual(solution(2468), 0)

    def test3(self):
        self.assertEqual(solution(11111), 1)

    def test4(self):
        self.assertEqual(solution(10), 1)

    def test5(self):
        self.assertEqual(solution(39991), 2187)

    def test6(self):
        self.assertEqual(solution(73004), 21)

    def test7(self):
        self.assertEqual(solution(123456), 15)

    def test8(self):
        self.assertEqual(solution(77777), 16807)

    def test9(self):
        self.assertEqual(solution(33333333), 6561)

    def test10(self):
        self.assertEqual(solution(100000000), 1)


if __name__ == "__main__":
    unittest.main()
