class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        res = set()
        set_1 = set(nums1)
        set_2 = set(nums2)
        set_3 = set(nums3)

        for num in set_1:
            if num in set_2 or num in set_3:
                res.add(num)
        for num in set_2:
            if num in set_1 or num in set_3:
                res.add(num)
        for num in set_3:
            if num in set_2 or num in set_1:
                res.add(num)

        return list(res)


# Optimal Solution:
from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)

        # Intersect pairs to find common elements, then union them together
        return list((s1 & s2) | (s1 & s3) | (s2 & s3))


# # Intuition
# To find values that appear in at least two out of the three arrays, we need to look for overlaps. Since duplicate elements within a single array do not matter for this condition, converting each list into a set allows us to focus entirely on unique values and perform rapid membership checks.

# # Approach
# 1. Convert `nums1`, `nums2`, and `nums3` into individual sets (`set_1`, `set_2`, `set_3`) to eliminate internal duplicates and enable O(1) lookup times.
# 2. Initialize an empty result set `res` to collect numbers that meet the condition.
# 3. Iterate through each unique number in `set_1`. If that number exists in `set_2` or `set_3`, add it to `res`.
# 4. Repeat this check for elements in `set_2` (against `set_1` or `set_3`) and elements in `set_3` (against `set_2` or `set_1`).
# 5. Convert the final `res` set back into a list and return it.

# # Complexity
# - Time complexity:
# \[O(N_1 + N_2 + N_3)\]
# Converting the lists to sets takes linear time relative to the size of each list. Iterating through the sets and checking membership takes O(1) average time per element, meaning the total time scales linearly with the total number of inputs.

# - Space complexity:
# \[O(N_1 + N_2 + N_3)\]
# In the worst-case scenario where all elements in the input arrays are unique, the space required to store `set_1`, `set_2`, `set_3`, and the final result set `res` will scale linearly with the total number of input elements.

# # Code
# ```python3 []
# class Solution:
#     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         res = set()
#         set_1 = set(nums1)
#         set_2 = set(nums2)
#         set_3 = set(nums3)

#         for num in set_1:
#             if num in set_2 or num in set_3:
#                 res.add(num)
#         for num in set_2:
#             if num in set_1 or num in set_3:
#                 res.add(num)
#         for num in set_3:
#             if num in set_2 or num in set_1:
#                 res.add(num)

#         return list(res)
# ```
