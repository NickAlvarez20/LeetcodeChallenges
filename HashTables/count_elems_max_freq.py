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


# Refactored:
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = Counter(nums).values() # Creates an array of max values/frequencies e.g., [2,2,1,1]
        max_freq = max(frequencies) # Sets max_freq for determining comparison operators
        return sum(f for f in frequencies if f == max_freq) # sums each individual elem using sum method if match found
