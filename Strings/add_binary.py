class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)
        sumBinary = decimal_a + decimal_b
        BinaryForm = bin(sumBinary)
        return BinaryForm[2:]


# Intuition
# At first the problem seems tricky because the strings can be very long (Up to 10,000 characters. ).
# -However, Python's int type supports arbitrary precision arithmetic, so we can:
# 1. Convert both binary strings to integers using base 2.
# 2. Perform Normal edition.
# 3. Convert the result back to binary string.
# 4. This approach is simple and readable, though it skips the manual bit by bit addition logic.
# Approach
# 1. Use int string, comma two to convert each binary string to its decimal integer value.
# 2. Add the two integers.
# 3. Use bin() To convert the sum back to a binary string.
# 4. Slice off the '0b' prefix that bin() adds.
# 5. Return the resulting string.
# Time complexity: O(n)
# 1. Converting a string of length n to int: O(n)
# 2. Converting the sum back to binary: O(m) Where M is the bit length of the sum (≈ max(len(a), len(b)) + 1)
# 3. Overall: O(n) Where n = max(len(a), len(b))
# Space complexity: O(n)
# 1. The integer representations internally use O(n) space for large numbers.
# 2. The output string is O(n)
# 3. Total extra space: (excluding output): O(n)

# Alternative methods:

# Approach 1: Optimal manual addition - Iterate from the end (Recommended for learning / interviews)
# Time Complexity: O(n) where n = max(len(a), len(b))
# Space Complexity: O(1) auxiliary (excluding the output string)
#
# Idea: Simulate grade-school binary addition from right to left, tracking a carry.
# 1. Use two pointers starting at the end of each string.
# 2. In a loop, add corresponding bits plus the carry.
# 3. Append the current bit (total % 2) to the result.
# 4. Update carry (total // 2).
# 5. Continue until both strings are processed and carry is 0.
# 6. Reverse the result at the end (or build it in reverse).
# This is the most efficient and educational approach: single pass, constant extra space,
# and works in any language without relying on big-integer support.

# Approach 2: One-liner using built-in functions (Most concise Pythonic solution)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Idea: Exactly what we have above — leverage Python's arbitrary-precision ints.
# Clean one-liner version:
#     return bin(int(a, 2) + int(b, 2))[2:]
# Very readable and concise. Automatically handles all edge cases (including a="0", b="0").
# Preferred in real-world Python code when performance isn't critical and readability matters.
# Note: This is acceptable on LeetCode for Python submissions, but interviewers may expect the manual version
# to demonstrate bit manipulation understanding.

# Summary
# - The current solution (big-int conversion) is correct, clean, and Pythonic.
# - For learning bit operations or interviews, prefer the manual carry-based iteration (Approach 1).
# - Both achieve the required O(n) time; manual version wins on space efficiency.
