from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq_dict = Counter(nums)
        for key, value in freq_dict.items():
            if value > len(nums) // 2:
                return key
        return 0


# Time Complexity - O(n)
# Creating the counter numbs object requires a single Passover the input list of size and resulting in O of n time
# The for loop iterates through the unique keys in the dictionary in the worst case if most elements are unique there are up to N keys but the total number of operations remains proportional to N
# Each dictionary look up in comparison within the loop takes O of constant time average

# Space Complexity - O(n)
#So the dictionary is open as we have to build it out so this results in o of n