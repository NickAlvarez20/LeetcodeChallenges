import unittest
from cosmo import solution


class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(12345), 54321)

    def test2(self):
        self.assertEqual(solution(1), 1)

    def test3(self):
        self.assertEqual(solution(87654321), 12345678)

    def test4(self):
        self.assertEqual(solution(54321), 12345)

    def test5(self):
        self.assertEqual(solution(87654321), 12345678)

    def test6(self):
        self.assertEqual(solution(56), 65)

    def test7(self):
        self.assertEqual(solution(4567890), 987654)

    def test8(self):
        self.assertEqual(solution(98765), 56789)

    def test9(self):
        self.assertEqual(solution(876), 678)

    def test10(self):
        self.assertEqual(solution(23456789), 98765432)


if __name__ == "__main__":
    unittest.main()
