# Intuition
# The intuition is a mathematical approach using a formula although the other method you could do this is with 2 pointers I found it much easier to just use a mathematical formula to check and an edge case

# Approach
# So the first thing we want to do is create a variable for the length of end store it for cleaner code and then do an edge case check if it's less than or equal to one we return 0 as this indicates there's a match and it's at the one position Later on our edge case will return -1 so it accounts for both of those situations. Then we loop through and find if the condition exists by looping through range and length and using the index to apply it to the string and then we check at the current position if it's equal to the length minus I - 1 we can return the smallest index with I.


# Complexity
# - Time complexity: O(N)
# The time complexity is O of N or linear time complexity as the string length scales we're just doing a simple loop.


# - Space complexity:
# The space complexity is all of one are constant We are not building any additional data structures arrays list We simply do it in place.


class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        # length var for clean code
        n = len(s)
        # edge case for optimal performance
        if len(s) <= 1:
            return 0
        # loop through and find if condition exists
        for i in range(len(s)):
            if s[i] == s[n - i - 1]:
                return i
        return -1
