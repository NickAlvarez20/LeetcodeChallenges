import unittest
from solution import reversed_triple_chars


class TestReversedTripleChars(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reversed_triple_chars("abcdef"), "cbafed")

    def test_2(self):
        self.assertEqual(reversed_triple_chars("s"), "s")

    def test_3(self):
        self.assertEqual(
            reversed_triple_chars("reversedtriplechars"), "versretdepircelrahs"
        )

    def test_4(self):
        self.assertEqual(reversed_triple_chars("abc"), "cba")

    def test_5(self):
        self.assertEqual(reversed_triple_chars("hello"), "lehlo")

    def test_6(self):
        self.assertEqual(reversed_triple_chars("abcdefg"), "cbafedg")

    def test_7(self):
        self.assertEqual(reversed_triple_chars("hellopython"), "lehpolhtyon")

    def test_8(self):
        self.assertEqual(reversed_triple_chars("ab"), "ab")


if __name__ == "__main__":
    unittest.main()
