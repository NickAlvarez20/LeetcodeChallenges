# Memoization

class Solution:
    def __init__(self):
        self.power = {}

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0 or n <= 0:
            return False

        # if calculated return this
        if n in self.power:
            return self.power[n]

        # otherwise calculate
        self.power[n] = self.isPowerOfTwo(n // 2)
        return self.power[n]

# Iteration