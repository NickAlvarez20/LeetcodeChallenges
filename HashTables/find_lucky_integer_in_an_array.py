# # Intuition
# So the key here is to use a frequency dictionary but you have to be mindful that is a trick question because it ask you to find a frequency in the array that's equal to its value. However using a frequency dictionary with a Max method will yield the correct value

# # Approach
# First thing we need to do is initialize 2 variables one is a frequency dictionary and the other sets the current Max to -1 to account for the edge case constraint. 2. Next we iterate using dot items method to look through the keys and the values. 3. Then we want to check conditionally if the key is equal to the value this will yield a lucky number. 3. Then we check and update current Max to the Max of the current Max that we're looking at against the key. What this does is it allows us to look at the current maximum and we compare it against the current key For example if we have current Max lucky number at two and we find a higher key value with a lucky number then we will return the Max so in this case comparing it to 4 we would return the 4. 4. Finally we return the current Max. 

# # Complexity
# - Time complexity:
# Creating the counter takes over in time to read the array iterating through the dictionary items takes O of U term where U is the number of unique elements total time is O of N + U which simplifies to O of N. 

# - Space complexity:
# This is O of N because In the worst case we'll have unique numbers for the entire ray so the dictionary will store it n keys. 

# Code
```python3 []
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_ints = Counter(arr)
        curr_max = -1

        for key, value in count_ints.items():
            if key == value:
                curr_max = max(curr_max, key)
            
        return curr_max
```