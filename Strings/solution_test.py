import unittest
from solution import repeat_char_jump


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(repeat_char_jump("abcdefg", 3), "adgcfbe")

    def test2(self):
        self.assertEqual(repeat_char_jump("a", 1), "a")

    def test3(self):
        self.assertEqual(repeat_char_jump("av", 1), "av")

    def test4(self):
        self.assertEqual(repeat_char_jump("cgldxdv", 4), "cxgdlvd")

    def test5(self):
        self.assertEqual(repeat_char_jump("z", 1), "z")

    def test6(self):
        self.assertEqual(repeat_char_jump("aaa", 2), "aaa")

    def test7(self):
        self.assertEqual(
            repeat_char_jump("zyxwvutsrqponmlkjihgfedcba", 5),
            "zupkfavqlgbwrmhcxsnidytoje",
        )

    def test8(self):
        self.assertEqual(
            repeat_char_jump("zyxwvutsrqponmlkjihgfedcba", 15),
            "zkvgrcnyjufqbmxitepalwhsdo",
        )

    def test9(self):
        self.assertEqual(repeat_char_jump("abcdefghij", 1), "abcdefghij")

    def test10(self):
        self.assertEqual(repeat_char_jump("abcdefghij", 9), "ajihgfedcb")


if __name__ == "__main__":
    unittest.main()
