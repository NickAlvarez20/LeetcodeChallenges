import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([3, 4, 5, 1, 2], 6))

    def test2(self):
        self.assertEqual(solution([1, 2], [2, 1]), ([2, 1], 0))

    def test3(self):
        self.assertEqual(solution([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], 0))
        
    def test4(self):
        self.assertEqual(solution([1, 2, 3], [2, 3, 1]), ([2, 3, 1], 0))
        
    def test5(self):
        self.assertEqual(solution([1], [1]), ([1], 0))

    def test6(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45))


if __name__ == '__main__':
    unittest.main()