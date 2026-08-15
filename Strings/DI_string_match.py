# # Intuition
# Intuition behind this greedy approach is to always pick the safest possible number for your available pool to guarantee the next constraint I for increase or D for decrease this met regardless of what letter follows by using 2 pointers low and high you maintain a range of remaining valid numbers at each step you make a choice that leaves the maximum possible flexibility for the remaining sequence. 

# # Approach
# 1. So first we initialize a low and high pointer and a result empty variable, 
# 2. Next we will loop through characters in the string
# 3. Then we want to check if the character is I, if it is update append the low to result and increase it by one
# 4. And then we check if the character is D then we can append the high and decrement it by one . By initializing it to the length of the string in the beginning we can ensure that we go from zero to the range correctly updating the maximum and minimum for each sequence within that range. 
# 5. At the end of this loop we'll have Remaining numbers so we want to make sure to append the low.
# 6. Finally we return the results

# # Complexity 
# - Time complexity: O (N)
# The largest part of the algorithm is the for loop and it loops for any given length of s. We are also updating the result list with the numbers at each sequence until we exhaust the list. This results in algorithm that scales linearly with the size of S. 

# - Space complexity: O(N)
# The result list scales linearly with the size of s. Low High in results are all initialized with O 1 constant space. As we build the results list this is going to be O of in auxiliary space for any given length of size S. 

# Code
```python3 []
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s) # 4 letters
        result = []

        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            elif char == "D":
                result.append(high)
                high -= 1
        result.append(low)

        return result



```