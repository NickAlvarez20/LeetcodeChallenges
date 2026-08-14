from itertools import combinations
import numpy as np

# first solution

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        def get_all_subsets(elements):
            subsets = []

            # Loop through all possive lengths of subsets
            for r in range(len(elements) + 1):
                subsets.extend(combinations(elements, r))
            return [list(subset) for subset in subsets]

        subset_list = get_all_subsets(nums)
        max_subset_or = 0

        # Find max bitwise OR of a subset
        for subset in subset_list:
            arr = np.array(subset, dtype=int)
            curr_val = np.bitwise_or.reduce(arr, initial=0)
            max_subset_or = max(max_subset_or, curr_val)

        count = 0

        for subset in subset_list:
            arr2 = np.array(subset, dtype=int)
            curr_val_2 = np.bitwise_or.reduce(arr2, initial=0)
            if curr_val_2 == max_subset_or:
                count += 1
        return count


