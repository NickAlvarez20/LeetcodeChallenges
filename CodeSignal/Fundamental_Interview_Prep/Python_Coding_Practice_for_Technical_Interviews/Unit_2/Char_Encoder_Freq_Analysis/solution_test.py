import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("Hello, 123!"), [47, 48, 49, 70, 99, 105, 109])

    def test_2(self):
        self.assertEqual(solution("Once upon a time, in a galaxy far, far away..."), [77, 97, 98, 99, 101, 102, 106, 106, 107, 109, 110, 111, 114, 114, 115, 117, 118, 118])

    def test_3(self):
        self.assertEqual(solution("When in the course of human events..."), [85, 95, 97, 100, 100, 103, 105, 107, 108, 112, 112, 113, 114, 116, 121])

    def test_4(self):
        self.assertEqual(solution("The quick brown fox jumps over the lazy dog."), [82, 96, 97, 97, 98, 100, 101, 101, 103, 104, 105, 106, 106, 107, 108, 110, 111, 111, 113, 114, 114, 116, 117, 118, 119, 120, 121])

    def test_5(self):
        self.assertEqual(solution("1234567890 abcdefghijklmnopqrstuvwxyz"), [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])

    def test_6(self):
        self.assertEqual(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89])

    def test_7(self):
        self.assertEqual(solution("fedcba"), [96, 97, 98, 99, 100, 121])

    def test_8(self):
        self.assertEqual(solution("This is a test."), [82, 99, 102, 102, 111, 113, 121])

    def test_9(self):
        self.assertEqual(solution("Test 123"), [47, 48, 49, 82, 99, 113, 114])

if __name__ == '__main__':
    unittest.main()