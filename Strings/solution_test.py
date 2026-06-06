import unittest
from solution import encode_rle


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(encode_rle("aabbbcceddf"), "a2b3c2e1d2f1")

    def test2(self):
        self.assertEqual(encode_rle("aaa@@bb!!c#d**e"), "a3b2c1d1e1")

    def test3(self):
        self.assertEqual(encode_rle("AA111bbbc"), "A213b3c1")

    def test4(self):
        self.assertEqual(encode_rle("a"), "a1")

    def test5(self):
        self.assertEqual(
            encode_rle("AAABCC@@@D123df#$@# adedfeee333!!!!!FFFFFFF"),
            "A3B1C2D1112131d1f1a1d1e1d1f1e333F7",
        )

    def test6(self):
        self.assertEqual(
            encode_rle(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            ),
            "a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z101112131415161718191",
        )

    def test7(self):
        self.assertEqual(encode_rle(""), "")

    def test8(self):
        self.assertEqual(encode_rle("1"), "11")

    def test9(self):
        self.assertEqual(encode_rle("11111111112222222222aaaaaaaaaaa"), "110210a11")

    def test10(self):
        self.assertEqual(
            encode_rle("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"),
            "A1a1B1b1C1c1D1d1E1e1F1f1G1g1H1h1I1i1J1j1K1k1L1l1M1m1N1n1O1o1P1p1Q1q1R1r1S1s1T1t1U1u1V1v1W1w1X1x1Y1y1Z1z1",
        )


if __name__ == "__main__":
    unittest.main()
