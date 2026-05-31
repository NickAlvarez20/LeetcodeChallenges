import unittest
from cosmo import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertListEqual(
            solution([12, 21, 34, 43, 56, 65]),
            [(12, 21), (21, 12), (34, 43), (43, 34), (56, 65), (65, 56)],
        )

    def test2(self):
        self.assertListEqual(
            solution([10, 1, 20, 2]), [(10, 1), (1, 1), (20, 2), (2, 2)]
        )

    def test3(self):
        self.assertListEqual(solution([1234, 4321]), [(1234, 4321), (4321, 1234)])

    def test4(self):
        self.assertListEqual(solution([1111, 1111]), [(1111, 1111), (1111, 1111)])

    def test5(self):
        self.assertListEqual(
            solution([12345, 54321, 11111, 44444, 22222, 88888]),
            [
                (12345, 54321),
                (54321, 12345),
                (11111, 11111),
                (44444, 44444),
                (22222, 22222),
                (88888, 88888),
            ],
        )


if __name__ == "__main__":
    unittest.main()
