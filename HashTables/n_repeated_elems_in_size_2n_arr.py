from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_freq_dict = Counter(nums)
        n = 0
        for key, val in nums_freq_dict.items():
            if val != 1:
                n = key
        return n
