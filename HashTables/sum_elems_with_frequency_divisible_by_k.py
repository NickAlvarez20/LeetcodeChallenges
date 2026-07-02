from collections import Counter


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq_dict = Counter(nums)
        print(freq_dict)
        sum_elements = 0

        for key, val in freq_dict.items():
            if val % k == 0:
                sum_elements += key * val
        return sum_elements
