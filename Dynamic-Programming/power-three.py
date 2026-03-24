# Memoization
class Solution:
    def __init__(self):
        self.power = {}

    def isPowerOfThree(self, n: int) -> bool:
        # Memoization: DP Approach
        # Establish base cases
        if n == 1:
            return True
        if n % 3 != 0 or n <= 0:
            return False

        # check if calculated, if it is, return this
        if n in self.power:
            return self.power[n]

        # othwerwise calc
        self.power[n] = self.isPowerOfThree(n // 3)
        return self.power[n]


# Iteration
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Dynamic Programming Approach: Iterative

        # Establish base case
        if n <= 0:
            return False

        # solve sub problem, what is true base case?
        current = 1

        # while current is less than or equal to n, update current each iteration by 3
        while current < n:
            current *= 3

        return current == n
