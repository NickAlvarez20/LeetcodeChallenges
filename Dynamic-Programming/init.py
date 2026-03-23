# Dynamic Programming is about mastering the mindset of breaking a complex problem into smaller, overlapping subproblems and storing their results to avoid redundant work.
# Unlike Greedy algorithms, DP "looks back" and considers all possible previous states to ensure the global optimum is found, which often makes it more robust but more memory-intensive.

# How to recognize?
# 1. Overlapping subproblems: The problem can be broken down into subproblems which are reused several times.
# 2. Optimal Substructure: The optimal solution to the entire problem can be constructed from the optimal solutions of its subproblems.
# 3. Interview clues: Look for keywords like "number of ways", "min costs", or "max profit" where a simple greedy choice doesn't account for future consequences. If the constraints are small enouhg (e.g., N <= 10^3 or 10^4), DP is often the intended path

# 0/1 Knapsack	Decide whether to "include" or "exclude" an item to reach a target.	416. Partition Equal Subset Sum, 494. Target Sum
# Fibonacci Sequence	The current state depends on the immediate 1 or 2 previous states.	70. Climbing Stairs, 198. House Robber
# Longest Common Subsequence	Compare two strings/arrays to find a common property.	1143. Longest Common Subsequence, 300. Longest Increasing Subsequence
# Grid Pathfinding	Move through a 2D matrix to find a path with min/max cost.	62. Unique Paths, 64. Minimum Path Sum

# Understand the difference between memorization (top-down) and tabulation (bottom-up)

# Climbing stairs

# Use python built in cache for simplicity

# Memoization (Top-Down Approach)
from functools import lru_cache


class Solution:
    @lru_cache(None)  # This is the "Memoization" magic
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way to stay at step 1, 2 ways to reach step 2
        if n <= 2:
            return n

        # To reach step 'n', you came from either (n-1) or (n-2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Tabulation (Bottom-Up Approach)
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n

    # Create a table to store ways to reach each step
    dp = [0] * (n+1)
    dp[1] = 1 # Base case: 1 way to reach step 1
    dp[2] = 2 # Base case: 2 ways to reach step 2

    # Fill the table iteratively
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Tradeoffs between bottom up and top down? Bottom up is often faster and uses memory more predictably since there's no recursion overhead

# Key takeaways: avoids O(2^n) exponential time of simple recursion by storing subproblem results, reducing the complexity to O(n) "linear" time.

# Top-Down (Memoization)
# Method: Recusion + Cache
# Intuition: Solves only what is need
# Efficient: Slightly more overhead(recursion)

# Bottom-Up (Tabuulation)
# Iteration + Table
# Systematically solves everything
# Generally faster and safer for large n

