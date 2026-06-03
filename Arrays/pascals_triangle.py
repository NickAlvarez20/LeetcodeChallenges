class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            # Use two pointers to fill middle values
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle


# Problem: 118 - Pascal's Triangle
# Link: https://leetcode.com/problems/pascals-triangle/
# Approach:
#     - Build Pascal's Triangle iteratively, row by row
#     - Each row starts and ends with 1 (handled by initializing with [1]s)
#     - Middle elements are the sum of two adjacent elements from the previous row
#     - We use an implicit two-pointers technique:
#         • For each position j in the current row (j from 1 to i-1),
#           we look at triangle[i-1][j-1] (left pointer) and triangle[i-1][j] (right pointer)
#         • These two indices are always adjacent and move together as j increases
#         • This "sliding pair" of pointers efficiently computes each new value
#     - Based on the animation, you can see clearly they are asking for two pointers for intuition
#
# Time Complexity: O(n^2)
#     - Total number of elements across all rows is numRows(numRows+1)/2
#
# Space Complexity: O(n^2)
#     - Required to store the complete output triangle
#
# Edge Cases Considered:
#     - numRows == 1 → [[1]]
#     - numRows == 2 → [[1], [1,1]]
#     - Rows with only 1 or 2 elements → inner loop doesn't run (correctly leaves 1s)
#
# Alternative Approaches Considered:
#     - Recursive version (elegant but risks stack overflow)
#     - Using math.comb() for binomial coefficients (clean but hides the pattern)
#     - Dynamic Programming 
#
# Learned:
#     - The two-pointers idea applies beyond sorted arrays or sliding windows
#     - Here, it's used to traverse adjacent pairs in the previous row
#     - The pointers (j-1 and j) move in lockstep — a classic "adjacent pair" traversal
#     - This is simple, efficient, and perfectly captures the local dependency in Pascal's Triangle
