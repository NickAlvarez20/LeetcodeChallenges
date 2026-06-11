from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_freq_dict = Counter(nums)
        max = 0
        count = 0
        print(nums_freq_dict)

        for key, val in nums_freq_dict.items():
            if val > max:
                max = val

        for key, val in nums_freq_dict.items():
            if val == max:
                count += val
        return count
