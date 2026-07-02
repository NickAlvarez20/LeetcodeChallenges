from collections import Counter
from typing import List


class Solution:
    # Beginner Approach

    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            prefix_set = set()
            suffix_set = set()

            # Add elements of prefix to a set
            for j in range(0, i+1):
                prefix_set.add(nums[j])
            # Add elements of suffix to another set
            for j in range(i+1, n):
                suffix_set.add(nums[j])

            # Calc the differenece for this specific prefix size
            diff = len(prefix_set) - len(suffix_set)
            res.append(diff)

        return res



# Optimal Approach:
def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
    suffix_counts = Counter(nums)
    prefix_sum = set()
    res = []

    # 2. Walk through each item in the array
    for num in nums:
        prefix_sum.add(num)
        suffix_counts[num] -= 1
        if suffix_counts[num] == 0:
            del suffix_counts[num]

        res.append(len(prefix_sum) - len(suffix_counts))
        pass

    return res


# # Intuition
# The problem asks us to find the difference between the number of distinct elements before (and including) an index and the number of distinct elements after that index. To do this efficiently without re-counting from scratch at every index, we can maintain running trackers for both sides: a set for the unique elements seen so far on the left, and a frequency map for the elements remaining on the right.

# # Approach
# 1. Initialize `suffix_counts` using a `Counter` to track the frequency of every number in the input array `nums`. This represents all elements to the right before we start processing.
# 2. Initialize an empty set `prefix_sum` to track unique elements on the left side, and an empty list `res` to hold our answers.
# 3. Iterate through `nums` element by element. For each element:
#    - Add it to the `prefix_sum` set to track it as a distinct prefix element.
#    - Decrement its frequency in `suffix_counts` because it is no longer part of the strict suffix.
#    - If its count drops to 0, completely remove it from `suffix_counts` so that `len(suffix_counts)` accurately reflects the number of unique elements left.
#    - Calculate the difference between the sizes of the prefix set and suffix counter, then append it to `res`.
# 4. Return the completed `res` list.

# # Complexity
# - Time complexity:
# \[O(N)\]
# We build the initial `Counter` in O(N) time, where N is the length of `nums`. Then, we iterate through the list exactly once. Inside the loop, set insertions, dictionary lookups, and deletions all take O(1) average time, making the total time complexity linear.

# - Space complexity:
# \[O(N)\]
# In the worst-case scenario where all elements in `nums` are unique, the `prefix_sum` set, `suffix_counts` dictionary, and the final `res` list will each store up to N elements.

# # Code
# ```python3 []
# from collections import Counter
# from typing import List


# class Solution:

#     def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
#         suffix_counts = Counter(nums)
#         prefix_sum = set()
#         res = []

#         # Walk through each item in the array
#         for num in nums:
#             prefix_sum.add(num)
#             suffix_counts[num] -= 1
#             if suffix_counts[num] == 0:
#                 del suffix_counts[num]

#             res.append(len(prefix_sum) - len(suffix_counts))

#         return res
# ```
