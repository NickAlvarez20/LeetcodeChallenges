import unittest
from solution import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("12345", "1234"), 1)

    def test2(self):
        self.assertEqual(solution("1234", "12345"), -1)

    def test3(self):
        self.assertEqual(solution("12345", "12345"), 0)

    def test4(self):
        self.assertEqual(solution("100", "101"), -1)

    def test5(self):
        self.assertEqual(solution("500", "500"), 0)

    def test6(self):
        self.assertEqual(solution("105382", "105383"), -1)

    def test7(self):
        self.assertEqual(solution("99999999999999999999", "100000000000000000000"), -1)

    def test8(self):
        self.assertEqual(solution("100000000000000000000", "99999999999999999999"), 1)

    def test9(self):
        self.assertEqual(solution("1", "1"), 0)


if __name__ == "__main__":
    unittest.main()
