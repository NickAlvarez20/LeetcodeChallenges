class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0
        right = len(nums) - 1
        avgs = []

        for i in range(len(nums) // 2 + len(nums) % 2):
            sum = (nums[left] + nums[right]) / 2
            avgs.append(sum)
            left += 1
            right -= 1

        return min(avgs)
