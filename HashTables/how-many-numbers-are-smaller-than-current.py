class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = []
        for i in range(len(nums)):
            curr_count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    curr_count += 1
            counts.append(curr_count)
        return counts
