import unittest
from solution import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solution("abcdef", [10, 20, 30, 40, 50, 60]), ("", [10, 20, 30, 40, 50, 60])
        )

    def test2(self):
        self.assertEqual(
            solution("xyzabc", [10, 20, 30, 40, 50, 60]), ("wxy", [40, 50, 60])
        )

    def test3(self):
        self.assertEqual(solution("bcdefg", [30, 40, 35]), ("ab", [35]))

    def test4(self):
        self.assertEqual(
            solution("xyzxyz", [10, 20, 30, 40, 50, 60]), ("wxy", [40, 50, 60])
        )

    def test5(self):
        self.assertEqual(solution("abc", [200]), ("", [200]))

    def test6(self):
        self.assertEqual(solution("z", [50]), ("y", []))


if __name__ == "__main__":
    unittest.main()
