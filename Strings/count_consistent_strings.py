# Intuition: Brute force approach where we loop through the initial word and then we have to loop through the individual characters within that word Also a Boolean and a total counter

# Approach: First we declare a total variable set it equal to 0 and then we loop through the word in the words list to get each individual index We actually use the exact value and not the index so we grab the value we set is within true for each part of this loop and then we go into the nested logic for character in the word that we are currently tracking we want to see if any character within this individual word is not in the allowed list If that is true we set is within the false for any detection then we break out If we get past this logic block then that means is within is actually true and we increment the total We repeat this process until we find the total that are set to true and we return that

# Complexity:
# Time: O(n^2)
# The time complexity since we are using a brute force approach is exponential O of N^2
# Space: O(1)
# There is of constant space because we are not creating any extra data types or data structures Therefore it is constant


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = 0
        for word in words:
            is_within = True
            for char in word:
                if char not in allowed:
                    is_within = False
                    break
            if is_within:
                total += 1
        return total
