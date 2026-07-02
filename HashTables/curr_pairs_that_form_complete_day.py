class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        total_count = 0

        for i in range(len(hours)):
            for j in range(len(hours)):
                if i < j and (hours[i] + hours[j]) % 24 == 0:
                    total_count += 1

        return total_count


# Optimized solution
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_counts = {}
        total_count = 0

        for hour in hours:
            rem = hour % 24
            # Find the needed remainder to make a multiple of 24
            complement = (24 - rem) % 24

            # If the complement exists in our map, add its frequency to our count
            if complement in remainder_counts:
                total_count += remainder_counts[complement]

            # Store or update the current remainder frequency
            remainder_counts[rem] = remainder_counts.get(rem, 0) + 1

        return total_count


# # Intuition
# The straightforward way to solve this problem is to check every possible pair of hours in the array. If the sum of any two distinct hours is perfectly divisible by 24, they form a complete day and should be counted.

# # Approach
# 1. Initialize a counter `total_count` to 0.
# 2. Use two nested loops to iterate through all possible pairs of indices `i` and `j`.
# 3. Apply the condition `i < j` to ensure each unique pair is checked exactly once and an element is not paired with itself.
# 4. Check if `(hours[i] + hours[j]) % 24 == 0`.
# 5. If true, increment `total_count` by 1.
# 6. Return the final `total_count`.

# # Complexity
# - Time complexity:
# \[O(n^2)\]
# We use two nested loops that both iterate up to the length of the array, resulting in a quadratic number of pair comparisons.

# - Space complexity:
# \[O(1)\]
# The algorithm only uses a few primitive variables (`total_count`, `i`, `j`) for tracking state, requiring no extra memory relative to input size.

# # Code
# ```python3 []
# class Solution:
#     def countCompleteDayPairs(self, hours: List[int]) -> int:
#         total_count = 0

#         for i in range(len(hours)):
#             for j in range(len(hours)):
#                 if i < j and (hours[i] + hours[j]) % 24 == 0:
#                     total_count += 1

#         return total_count
# ```
