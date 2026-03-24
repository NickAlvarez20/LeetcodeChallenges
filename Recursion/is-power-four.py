class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 4 != 0 or n <= 0:
            return False

        return self.isPowerOfFour(n // 4)


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
        self.power[n] = self.isPowerOfFour(n//4)
        return self.power[n]
