# Intuition
# So the first step is to use a frequency counter and check if the value has an odd count flag. We can check the value if it's even, we can add it. If it is odd, we can use a modulo operator. Then add one for whatever is remaining that has an odd count. 

# Approach
# 1. Create a frequency counter with importing Counter from collections. 
# 2. Create a length and has odd count variable. 
# 3. Create an iteration loop for key value using .items to check within each of the items key value pairs within frequency Counter hash Map. 
# 4. Update the length with the current value divided by 2 and then multiply it by 2. 
# 5. Add a conditional check. If value modulo 2 equals 1, set the has odd count flag to true. 
# 6. Then we can increment the length plus equals 1 for each situation that this occurs within the current hash map. 
# 7. Finally, return the length. 

# Complexity
# - Time complexity: O(N)
# The time complexity, considering an initial string of length s and a frequency counter dictionary for any given length s, and then iterating through the items within the frequency count dictionary for any given length, is O(n). 

# - Space complexity: O(N)
# The main space complexity is creating the frequency dictionary using a counter, so that would allocate O of n memory for any given input size of s. The other considerations are creating a length and has odd count flag variable, which are O of 1 space complexities. Finally, as we update and iterate with the for loop, we are incrementing length with two checks, which is also O of 1 space. So overall the total space complexity is O of n. Now the correct and preferred answer is O(1) because in most LeetCode problems the input string S consists only of lowercase and uppercase English letters. This means the HashMap will never hold more than 52 unique keys, no matter how long the string is. Because the memory usage is capped at a fixed maximum size, the space complexity is technically O(1) space. 
# 

# Code

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_count = Counter(s)
        length = 0
        has_odd_count = False

        for key, val in freq_count.items():

            length += (val//2) * 2

            if val % 2 == 1:
                has_odd_count = True

        if has_odd_count:
            length += 1

        return length

            

        
        


        

