# Intuition: We can use a greedy approach using balance counter to split balance strings a balance string means the number of left and right characters are equal while traversing the string we can treat left as plus one and right as -1 whenever the balance becomes zero it means we have equal numbers of left and right in that segment so each time the balance becomes zero we find one balance substring and we increment the count

# Approach:
# 1. We initialize balance and count and set them equal to zero
# 2. Iterate through the entire range length of the given string
# 3. First check during the initial part of the loop if balance equals 0 for each iteration If balance equals zero we can increase the count by one 
# 4. Next we check if the current value is equal to left if it is we increase the balance by 1 and then we also check if the current value is equal to right then we will decrement by 1 
# 5. Finally we can return the count at the end and this will be the correct amount of substrings that are balanced
# Complexity:
# Time: O(n)
# The time complexity is O of N since we iterate through the entire string once, linear
#
# Space: O(1)
# We only use two integer variables therefore the time space complexity is of one or constant space complexity. 

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for i in range(len(s)):
            if balance == 0:
                count += 1
            if s[i] == "L":
                balance += 1
            if s[i] == "R":
                balance -= 1
        return count
