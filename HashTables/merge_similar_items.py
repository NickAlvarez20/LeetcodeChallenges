from collections import Counter


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        res = []
        counter_dict = Counter()

        # Create two frequency arrays and add all values with matching keys
        for key, val in items1:
            counter_dict[key] += val
        for key, val in items2:
            counter_dict[key] += val
        for key, val in counter_dict.items():
            res.append([key, val])
        return sorted(res)

# Optimal Solution
from typing import List


class Solution:

    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        # 1. Initialize a fixed rack of weights from index 0 to 1000
        # This provides instant O(1) random access
        weights = [0] * 1001

        # 2. Add weights directly to their respective value indexes
        for value, weight in items1:
            weights[value] += weight

        for value, weight in items2:
            weights[value] += weight

        # 3. Collect non-zero slots. They are already in perfect ascending order!
        return [[val, weights[val]] for val in range(1001) if weights[val] > 0]


# # Intuition
# The problem requires combining weights for items with matching values and returning them in ascending order of their values. Since we need to aggregate values based on unique keys, a hash map (or Counter) is a natural fit to automatically group and sum the weights as we iterate through both lists.

# # Approach
# 1. Initialize an empty `Counter` dictionary to map each item's value (key) to its total weight (val).
# 2. Loop through `items1` and add each item's weight to its corresponding key in the counter.
# 3. Loop through `items2` and similarly accumulate those weights into the same counter.
# 4. Iterate through the unique keys and combined weights in the counter, appending each pair as a list `[key, val]` into a result array `res`.
# 5. Sort the result array so that the items are ordered by their values in ascending order, and return it.

# # Complexity
# - Time complexity:
# \[O((N + M) \log(N + M))\]
# Populating the hash map takes linear time \(O(N + M)\), where \(N\) and \(M\) are the lengths of `items1` and `items2`. Extracting the entries and sorting them by their keys takes \(O(U \log U)\) time, where \(U\) is the number of unique item values. In the worst-case scenario where all item values are unique, \(U = N + M\).

# - Space complexity:
# \[O(N + M)\]
# The hash map stores up to \(N + M\) unique key-value pairs in the worst case. The result array `res` also holds up to \(N + M\) lists before it is sorted and returned.

# # Code
# ```python3 []
# from collections import Counter

# class Solution:
#     def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
#         res = []
#         counter_dict = Counter()

#         # Create two frequency arrays and add all values with matching keys
#         for key, val in items1:
#             counter_dict[key] += val
#         for key, val in items2:
#             counter_dict[key] += val
#         for key, val in counter_dict.items():
#             res.append([key, val])
#         return sorted(res)
# ```
