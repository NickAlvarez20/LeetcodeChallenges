# placeholderimport unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        arrayA = [2, 1, 3, 0]
        arrayB = [1, 3, 2, 4]
        arrayC = [4, 2, 5, 1]
        result = solution(arrayA, arrayB, arrayC)
        self.assertEqual(result, 7)  # maximum value in arrayB is 3 and arrayC is 4

    def test_2(self):
        arrayA = [2, 0, 1]
        arrayB = [1, 3, 2]
        arrayC = [2, 0, 1]
        result = solution(arrayA, arrayB, arrayC)
        self.assertEqual(result, 2)

    def test_3(self):
        arrayA = [1, 1, 0]
        arrayB = [2, 1, 3]
        arrayC = [2, 0, 1]
        result = solution(arrayA, arrayB, arrayC)
        self.assertEqual(result, 1)

    def test_4(self):
        arrayA = [0, 2, 0]
        arrayB = [1, 1, 2]
        arrayC = [0, 1, 2]
        result = solution(arrayA, arrayB, arrayC)
        self.assertEqual(result, 3)

    def test_5(self):
        arrayA = [1, 1, 2, 0]
        arrayB = [2, 2, 1, 3]
        arrayC = [1, 2, 3, 4]
        result = solution(arrayA, arrayB, arrayC)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
