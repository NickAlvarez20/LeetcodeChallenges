# # Intuition
# We can utilize a Hash Set to store all unique numbers from the input array. This allows us to instantly check if the negative counterpart of any given number exists in constant time, eliminating the need for a slow O(N^2) nested loop search.

# # Approach
# First we declare and we initialize Max K to -1 to account for the edge case constraint. 2. Next we iterate through the Set and then we use another conditional check to see if negative number is in set one so for each number we're checking if it has a negative equivalent within that set. If that condition is true we can update Max K with the Max and consider the argument as the current Max K and compare that to the current number. 3. Finally we return the Max K

# # Complexity
# - Time complexity: O (N)
# The time complexity is O of N for the given size of the set. Converting the list and into a set takes obe end time iterating through the set takes OB in time and checking membership takes over one constant time per element this results in a total time complexity of O(N)

# - Space complexity: O(N)
# We are only creating memory allocation for the set, Board stores up to N unique elements of the input array.


# Code
```python3 []
from collections import Counter

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        set1 = set(nums)
        max_k = -1

        for num in set1:
            if -num in set1:
                max_k = max(max_k, num)
        return max_k


        
```