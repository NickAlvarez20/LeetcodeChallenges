import unittest
from solution import replace_substring

class ReplaceSubstringTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(replace_substring("hello world", "world", "friend"), "hello friend")

    def test_2(self):
        self.assertEqual(replace_substring("i love coding", "code", "craft"), "i love coding")

    def test_3(self):
        self.assertEqual(replace_substring("it is a beautiful day", "beautiful", "gloomy"), "it is a gloomy day")

    def test_4(self):
        self.assertEqual(replace_substring("practice makes perfect", "perfect", "better"), "practice makes better")

    def test_5(self):
        self.assertEqual(replace_substring("keep calm and carry on", "carry on", "code on"), "keep calm and code on")

    def test_6(self):
        self.assertEqual(replace_substring("long text long text", "long", "short"), "short text short text")

    def test_7(self):
        self.assertEqual(replace_substring("lower case", "lower", ""), " case")

    def test_8(self):
        self.assertEqual(replace_substring("a quick brown fox jumps over a lazy dog", "jumps", "skips"), "a quick brown fox skips over a lazy dog")

    def test_9(self):
        self.assertEqual(replace_substring("this is a test", "this", "that"), "that is a test")

    def test_10(self):
        self.assertEqual(replace_substring("final test case", "case", "example"), "final test example")

if __name__ == "__main__":
    unittest.main()