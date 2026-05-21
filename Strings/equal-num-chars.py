# Intuition
# No intuition is to use a frequency map or count and then the second thing is to use a set with a conditional check To leverage the unique property of a set. 

# Approach
# 1. First we create a frequency map by importing counter from collections.
# 2. Next we create a compare set variable and use a set with the frequency map and values notation
# 3. We then check if the length of the compare set is equal to one which will indicate that there's only one value stored in that set of values which will and should equal 1 if all values are the same
# 4. If there are equal to one we return true otherwise it's false

# Complexity
# - Time complexity: O(N)
# The operations for creating a frequency map and a set are O of N equal to the linear time complexity


# - Space complexity: O(N) or O(K) where K in the number of unique characters
# We create a frequency map and compare set and these each take up auxiliary space O of N for any given input size of the string. Since the input only contains lower case English letters that space is technically O of one constant because the alphabet is capped at 26. 


from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq_map = Counter(s)
        compare_set = set(freq_map.values())

        if len(compare_set) == 1:
            return True
        else:
            return False
