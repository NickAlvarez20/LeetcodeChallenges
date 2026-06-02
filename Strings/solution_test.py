import unittest
from solution import special_order

class SpecialOrderTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(special_order("abcde"), "edcab")

    def test_case_2(self):
        self.assertEqual(special_order("abcdef"), "fedabc")

    def test_case_3(self):
        self.assertEqual(special_order("a"), "a")

    def test_case_4(self):
        self.assertEqual(special_order("zyxwvutsrqpon"), "nopqrstzyxwvu")

    def test_case_5(self):
        self.assertEqual(special_order("abcddcba"), "abcdabcd")
    
    def test_case_6(self):
        self.assertEqual(
            special_order("abcdefghijklmnopqrstuvwxyz"*4 +"abcd"), 
            "dcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab"
        )

if __name__ == '__main__':
    unittest.main()