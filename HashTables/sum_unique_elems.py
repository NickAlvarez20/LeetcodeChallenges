from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_counts = Counter(nums)
        sum = 0

        for key, val in unique_counts.items():
            if val == 1:
                sum += key
        return sum
