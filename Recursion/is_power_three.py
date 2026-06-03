class Solution:
    def __init__(self):
        self.power = {}

    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 != 0 or n <= 0:
            return False
        return self.isPowerOfThree(n // 3)
