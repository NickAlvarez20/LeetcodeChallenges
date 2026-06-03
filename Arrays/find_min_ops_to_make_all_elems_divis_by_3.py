class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total_ops = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                total_ops += 1
        return total_ops
