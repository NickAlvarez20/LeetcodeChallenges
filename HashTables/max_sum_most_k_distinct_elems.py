class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # Create a set
        unique_nums = set(nums)
        sorted_uniques = sorted(unique_nums, reverse=True)

        return sorted_uniques[0:k]


# Optimal Solution:

import heapq
from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # Using heapq.nlargest automatically finds the top k largest in O(N log k)
        return heapq.nlargest(k, set(nums))


# # Intuition
# The goal is to find the k largest distinct elements from the given list. My first thought is to eliminate duplicate values immediately to ensure all elements are unique, and then sort them in descending order to easily pick the top k largest numbers.

# # Approach
# 1. Convert the input list `nums` into a Python `set` to automatically remove all duplicate elements.
# 2. Sort the unique elements in descending order using the `sorted()` function with `reverse=True`.
# 3. Use slicing `[0:k]` to extract and return the first k elements from the sorted list.

# # Complexity
# - Time complexity:
# \[O(n \log n)\]
# where n is the number of elements in the input list. Converting the list to a set takes O(n) time. Sorting the unique elements takes \(O(u \log u)\) time, where u is the number of unique elements (u ≤ n). Slicing takes O(k) time.

# - Space complexity:
# \[O(n)\]
# to store the unique elements in the set and the subsequent sorted list.

# # Code
# ```python3 []
# class Solution:
#     def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
#         # Create a set
#         unique_nums = set(nums)
#         sorted_uniques = sorted(unique_nums, reverse=True)

#         return sorted_uniques[0:k]

# ```
