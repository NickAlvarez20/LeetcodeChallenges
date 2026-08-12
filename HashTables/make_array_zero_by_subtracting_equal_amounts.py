# # Intuition
# So the first idea is to identify a minimum and then subtract that value and continue to find the minimum while subtracting from the array until the array equals zero for all values. Upon further inspection and research and reading the hint all you need to do is check for unique elements in the array So a set works wonders as long as you remove the zero So the most efficient way is to use the numpy library create a numpy array and then use Boolean indexing to remove all the zeros from that array and then create a set and check the length

# # Approach
# 1. So first you want to convert the original array into a numpy array. 2. Then you want to use boolean indexing to remove the zeroes from the array. 3. Next you want to create a set with that non zero array. 4. Finally you can return the length of that set and that will contain all unique values, Which optimally solves the problem in a very unique and creative way. 

# # Complexity
# - Time complexity: O(N) average, O(N^2) worst case. Reiterate through the list of size in exactly once. Inserting each element into the hash that takes of one time on average. 
# 

# - Space complexity: O(N)
# In the worst case scenario all elements in the array are unique and non zero requiring the set to store N elements. 

# Code
```python3 []
import numpy as np

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = np.array(nums)
        # remove all zeroes
        non_zero = arr[arr != 0]
        # create a set
        set_1 = set(non_zero)

        return len(set_1)


        
```