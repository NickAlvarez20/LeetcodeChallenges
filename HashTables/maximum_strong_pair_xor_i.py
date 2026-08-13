# Intuition
# So first we want to use a double nested brute force solution to find all the possible pairs. And then we want to loop through pair in pairs and do the initial strong pair conditional check. We also want to prevent duplicates so we'll be adding the strong pairs to a set. Then we want to ensure that we loop through and unpack the tuple within strong pairs that we are creating and then we do a XOR operation with the Max method and then we can find the Max Xor. 

# Approach
# 1. First we initialize the foundational variables so we create an empty array for pairs and an empty set for strong pairs
# 2. Next do a double nested for loop for I and ranging to the length of nums and then starting at I Then we append to the pairs list all the possible combinations of pairs that exist within that given list 
# 3. Then once we have the given list we want to check the pairs that exist to identify the strong pairs using the condition so we use an absolute value and check if it's less than or equal to the minimum of the 1st and second value if so we can add to strong pairs and add it to the set 
# 4. Then I set up a Max Azure variable and initialize it at zero value just for a global variable within the function
# 5. Next we want to unpack the tuple of strong pairs set for XY and strong pairs and then create a result variable and do the Azure operation Then we want to pass the result into our Max Azure where we're calculating using the Max method with the first argument being the current Magzor and the 2nd argument being the result that we have just calculated 
# 6. Finally we return the Max Xor and that will be the correct answer 

# Complexity
# - Time complexity: O(N^2):
# The maximum time complexity for this algorithm is O of N ^2 because we are using a double nested loop all the other iterations require only a single loop therefore the largest part of this algorithm is the double nested loop resulting in an O of N squared time complexity 

# - Space complexity: O(N^2)
# Because we append every possible pair to the pairs list the list grows quadratically a list of all pairs from an erase size of N requires N parentheses N + 1 / 2 elements which simplifies to O of N ^2 space. 


#. 

# Code
```python3 []
import itertools


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        pairs = []
        strong_pairs = set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                pairs.append((nums[i], nums[j]))

        for pair in pairs:
            if abs(pair[0] - pair[1]) <= min(pair[0], pair[1]):
                strong_pairs.add(pair)
        
        max_xor = 0

        for x, y in strong_pairs:
            res = x^y
            max_xor = max(max_xor, res)
        return max_xor

```


# To optimize the current approach to OH-1 auxiliary space by eliminating the intermediate pairs and strong pairs collection we can do this code below 
# class Solution:
#     def maximumStrongPairXor(self, nums: List[int]) -> int:
#         max_xor = 0
#         n = len(nums)
        
#         # Double nested loop checks pairs directly without storing them
#         for i in range(n):
#             for j in range(i, n):
#                 x, y = nums[i], nums[j]
                
#                 # Strong pair condition check
#                 if abs(x - y) <= min(x, y):
#                     max_xor = max(max_xor, x ^ y)
                    
#         return max_xor


# By sorting the array we can use a sliding window or a tree structure for bitwise maximization to find the pairs efficiently Here's the sliding window variant that minimizes unnecessary checks.

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()  # Sorting allows us to drop the abs() and min() checks
        max_xor = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i, n):
                if nums[j] > 2 * nums[i]:
                    break  # All subsequent elements will fail the condition
                max_xor = max(max_xor, nums[i] ^ nums[j])
                
        return max_xor
