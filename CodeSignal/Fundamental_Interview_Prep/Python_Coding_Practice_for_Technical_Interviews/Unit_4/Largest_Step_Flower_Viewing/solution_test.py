import unittest
from solution import largest_step

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(largest_step([3, 1, 2, 1, 3, 2, 1], 0, 1), 2)

    def test2(self):
        self.assertEqual(largest_step([1, 2, 3, 4, 5, 9, 2, 1, 3, 8, 2, 7, 1, 6], 13, -1), 1)

    def test3(self):
        self.assertEqual(largest_step([1, 2, 3, 4, 5], 0, 1), 1)

    def test4(self):
        self.assertEqual(largest_step([1], 0, 1), 1)

    def test5(self):
        self.assertEqual(largest_step([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, -1), -1)

    def test6(self):
        self.assertEqual(largest_step([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 9, -1), 1)

    def test7(self):
        self.assertEqual(largest_step([1, 2, 2, 4, 5, 5], 0, 1), 1)

    def test8(self):
        self.assertEqual(largest_step([1, 1, 1, 1, 2, 1], 0, 1), 4)

    def test9(self):
        self.assertEqual(largest_step([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, -1), -1)

    def test10(self):
        self.assertEqual(largest_step([1, 5, 2, 5, 3, 5, 4, 5], 3, -1), -1)

if __name__ == '__main__':
    unittest.main()