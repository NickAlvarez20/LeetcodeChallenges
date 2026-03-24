# Memoization
class Solution:
    def __init__(self):
        self.power = {}

    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 4 != 0 or n <= 0:
            return False

        # if calculated, return this
        if n in self.power:
            return self.power[n]

        # otherwise calc and store
        self.power[n] = self.isPowerOfFour(n // 4)
        return self.power[n]

# Iteration 

class Solution:
    def isPowerOfFour(self, n:int) -> bool:
        # Base case for non-positive numbers
        if n <= 0:
            return False
        
        # We can start at the smallest sub problem (4^0 = 1)
        current = 1

        # Iteratively build up to the powers of 4
        while current < n:
            current *= 4

        # iF WE LANDED EXACTLY ON N, it's a power of four
        return current == n