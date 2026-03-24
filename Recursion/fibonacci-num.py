# Intuition: Whenever you see a formula like F(n) = F(n-1) + F(n-2),
# your brain should immediately think:

# 1. Naive Recursion:
# Easy to write, but slow (O(2^n)).

# 2. Memoization (Top-Down):
# Keep the recursion, but add a dictionary to remember results (O(n) time).

# 3. Iteration (Bottom-Up):
# Use a loop and two variables to build the answer from 0 up to n
# (O(n) time, O(1) space).




# time O(N^2)
# For every call to fib(n), the function makes two more recursive calls: fib(n-1) and fib (n-2)
# space O(N) = While the total num of calls is exponential, the computer only needs to keep track of the current path down the recursion tree. The max depth of the recursion tree is n. At any given time, there are at most n function calls on the call stack.

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
