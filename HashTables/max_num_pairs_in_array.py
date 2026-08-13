# Intuition
# So at first I thought I could brute force the solution compare each number and then remove them from the list. Then I realized I could use a count and length check with counter dictionary to identify and correctly sort through while using a while loop This makes a lot more optimal and efficient so the intuition is to use a counter dictionary loop through using a for loop and then a while loop to evaluate the condition and remove the frequency count until it equals a certain condition while appending to two arrays.

# Approach
# 1. So first we initialize a counts frequency dictionary and input nums as the argument
# 2. Then we create a result and a second result array which will store the data we need
# 3. Then we use a four key value with items to access both the key the value using the dot items method for dictionary access.
# 4. Then I implement a while loop which checks the condition if the value is greater than one we want to repeat a certain amount of operations. 
# 4a. So for this operation until the condition is less than one we will append the key and decrement the value by 2
# 4ab. At the end of this if the value equals 1 after decrementation, We can update the second result array with the key which will be the last remaining number in the array .
# 4ab1. Then we decrement the value by one which will make the condition less than 1 and exit the while loop.
# 5. Finally this is where the final logical result happens; we want to return the length of the result and the length of the second result. 

# Complexity
# - Time complexity: O(N)
# The time complexity is O(N). 
# 1. The while loop only decrements value (the frequency of a number) The frequency of a number. The total sum of all values in dictionary is exactly N. 
# 2. Even though the loops are nested the inner wall loop can never run more times in total across the entire execution than our elements and nums.
# 3. Since every element from the original ray is processed a constant number of times the total time spent across all iterations of ball dudes combined is strictly bounded by O of N. 

# - Space complexity: O(N)
# 1. The counter dictionary is O of N for any given NUM's length. 2. We have resultant second result which are equivalent to the length of decrementation for the while loop so these are O of N. So the space allocation is O of N. The counter dictionary in the result arrays scale linearly with the number of unique elements bounding it to O of N. 

# Code
```python3 []
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []
        second_result = []
        for key, value in counts.items():
            while value > 1:
                result.append(key)
                value -= 2
            if value == 1:
                second_result.append(key)
                value -= 1


        return [len(result), len(second_result)]

            


        
```