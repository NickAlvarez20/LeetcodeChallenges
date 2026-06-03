import math


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        proper_range = []
        result = []
        for i in range(sorted_nums[0], sorted_nums[-1] + 1):
            proper_range.append(i)

        for num in proper_range:
            if num not in sorted_nums:
                result.append(num)
        return result
