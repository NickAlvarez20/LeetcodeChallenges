class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        total = 0
        n = len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0 <= i and i < j and j < n and nums[i] + nums[j] < target:
                    total += 1
        return total
