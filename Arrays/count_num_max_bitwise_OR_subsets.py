# Intuition
# The intuition behind this approach is to solve the problem by explicitly checking every single mathematical possibility Since a bitwise over operation could never decrease a value it only keeps or adds bits the maximum possible bitwise OR of any subset must be the resulting of ordering all numbers in the array together instead of using bit manipulation math to find that shortcut this solution takes a literal approach Generate every possible subset of the ray calcules the bit wires or value for each 1 using lumpy's vector reduction capabilities find the absolute maximum value produced and then filter and count how many subsets achieve that maximum 

# Approach
# 1. Use ittertools that combinations inside a loop ranging from length 0 to length gnomes to extract every possible combination of elements converting them into a master list of subsets
# 2. Find the maximum bitwise target iterate through every generated subset for each subset converted into a numpy array and utilize MP dot bitwise or dot reduce array initial set to zero to officially compute its cumulative bitwise or value track the highest value seen using the Max function.
# 3. Count the maxima iterate through the master list of subsets a second time recalculating each subset bitwise OR using the same number reduction method checking if it matches the Max subset or target if it matches incremental counter. 
# 4. Return the result return the final count of matching subsets

# # Complexity
# - Time complexity: O(2^N *N) 
# An array of size N has exactly two to the north total subsets. This code generates all two to the N subsets. Free subset which can be up to length and you can read it into a numpy array and compute the bitwise or. This takes OVID time per subset. Because you loop through the entire list of subsets twice this time scales as 2X2 to the N * N which simplifies to O of 2 N * N. 

# - Space complexity: O(2^N * N)
# you store all two to the end subsets inside the subset list of variables simultaneously.  Since each subset can hold up to N integers storing this full list of memory scales exponentially based on the input size dominating the space constraint. 

# To optimize: Combine the loops: You can find the maximum value and count it in a single pass instead of looping through subset_list twice.Eliminate NumPy/Itertools: You can use a recursive backtracking Depth-First Search (DFS) or bitmasking to compute the OR values on-the-fly. This would drop your space complexity from an exponential \(O(2^N \cdot N)\) all the way down to a linear \(O(N)\) for the recursion stack!

# Code
```python3 []
from itertools import combinations
import numpy as np

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def get_all_subsets(elements):
            subsets = []

            # Loop through all possive lengths of subsets
            for r in range(len(elements)+1):
                subsets.extend(combinations(elements, r))
            return [list(subset) for subset in subsets]

        subset_list = get_all_subsets(nums)
        max_subset_or = 0
        
        # Find max bitwise OR of a subset
        for subset in subset_list:
            arr= np.array(subset, dtype=int)
            curr_val = np.bitwise_or.reduce(arr, initial=0)
            max_subset_or = max(max_subset_or, curr_val)

        count = 0

        for subset in subset_list:
            arr2 = np.array(subset, dtype=int)
            curr_val_2 = np.bitwise_or.reduce(arr2, initial=0)
            if curr_val_2 == max_subset_or:
                count += 1
        return count
            



        
```