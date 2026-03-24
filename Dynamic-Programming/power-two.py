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
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Memoization:
        # Base case changes since we are simply multiplying
        if n <= 0:
            return False

        # Establish sub program starting point, for this it's one
        current = 1

        # While current is less than n, we need to multiply by two to determine if power of two is reached
        while current < n:
            current *= 2

        return current == n
