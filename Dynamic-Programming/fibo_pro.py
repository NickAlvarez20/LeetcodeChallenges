class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # If we already calculated this, just return it
        if n in self.memo:
            return self.memo[n]

        # Otherwise calc and store
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


# Time: O(n) - Each number is calculated exactly once.
# Space: O(n) - For the recursion stack and the dictionary.


# Iteration (Bottom up)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # a is fib(i-2), b if fib(i-1)
        a, b = 0, 1

        for _ in range(2, n+1):
            # Calc the next num and slide  window
            a, b = b, a+b
        return b