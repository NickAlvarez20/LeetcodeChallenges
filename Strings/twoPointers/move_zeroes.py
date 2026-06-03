class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0 and nums[left + 1] > 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[right] == 0 and nums[right - 1] > 0:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
        return nums
    
# Update: Perform time and space complexity analysis
