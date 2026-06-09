import unittest
from solution import solution


class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("hello world"), "Hello World")

    def test_2(self):
        self.assertEqual(solution("HELLO WORLD"), "Hello World")

    def test_3(self):
        self.assertEqual(solution("123 hello"), "123 Hello")

    def test_4(self):
        self.assertEqual(solution("_underscore"), "_underscore")

    def test_5(self):
        self.assertEqual(
            solution(
                "first second third fourth fifth sixth seventh eights ninth tenth"
            ),
            "First Second Third Fourth Fifth Sixth Seventh Eights Ninth Tenth",
        )

    def test_6(self):
        self.assertEqual(solution("single"), "Single")

    def test_7(self):
        self.assertEqual(
            solution("Hello neat pythonistas_123"), "Hello Neat Pythonistas_123"
        )

    def test_8(self):
        self.assertEqual(solution("SoME rAndoM _TeXT"), "Some Random _text")

    def test_9(self):
        self.assertEqual(solution("CAPS lock IS on"), "Caps Lock Is On")

    def test_10(self):
        self.assertEqual(solution("mIxEd CaSe sample"), "Mixed Case Sample")


if __name__ == "__main__":
    unittest.main()
