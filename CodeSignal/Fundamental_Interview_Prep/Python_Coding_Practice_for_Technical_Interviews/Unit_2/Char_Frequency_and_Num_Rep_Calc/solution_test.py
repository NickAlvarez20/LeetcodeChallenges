import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("abc"), {'a': 120, 'b': 121, 'c': 122})

    def test2(self):
        self.assertEqual(solution("def"), {'d': 97, 'e': 98, 'f': 99})

    def test3(self):
        self.assertEqual(solution("xyz"), {'x': 117, 'y': 118, 'z': 119})

    def test4(self):
        self.assertEqual(solution("aabccc"), {'a': 240, 'b': 121, 'c': 366})

    def test5(self):
        self.assertEqual(solution("abcdefghij"), {'a': 120, 'b': 121, 'c': 122, 'd': 97, 'e': 98, 'f': 99, 'g': 100, 'h': 101, 'i': 102, 'j': 103})

    def test6(self):
        self.assertEqual(solution("zzzzzzzzzz"), {'z': 1190})

    def test7(self):
        self.assertEqual(solution("abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"), {'a': 3600, 'b': 3630, 'c': 3660})

    def test8(self):
        self.assertEqual(solution("xyzaaxz"), {'a': 240, 'x': 234, 'y': 118, 'z': 238})


if __name__ == '__main__':
    unittest.main()