class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1
        # negative case
        if n < 0:
            return 1 / self.myPow(x, -n)

        # glue - sub problem
        half = self.myPow(x, n // 2)  # halving

        # if n is even or odd remainder
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
