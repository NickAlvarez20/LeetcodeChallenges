import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solution import tournament

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(tournament([100, 50, 30, 20]), 3)

    def test2(self):
        self.assertEqual(tournament([70, 80, 60]), 1)

    def test3(self):
        self.assertEqual(tournament([30, 20, 10, 40, 50]), 2)

    def test4(self):
        self.assertEqual(tournament([60, 70]), 1)
    
    def test5(self):
        self.assertEqual(tournament([50, 20, 30, 40]), 1)

    def test6(self):
        self.assertEqual(tournament([90, 10, 30]), 1)

    def test7(self):
        self.assertEqual(tournament([30, 100]), 1)

    def test8(self):
        self.assertEqual(tournament([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), 1)

    def test9(self):
        self.assertEqual(tournament([60, 40, 30, 20, 10]), 2)

    def test10(self):
        self.assertEqual(tournament([100]), 0)

    def test11(self):
        self.assertEqual(tournament([10, 10, 10]), 0)
        
if __name__ == '__main__':
    unittest.main()