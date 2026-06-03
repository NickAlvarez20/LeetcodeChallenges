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


# dictionary and prefix sum approach : butter algorithms

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # sort the unique nums
        sorted_keys = sorted(counts.keys())

        smaller_counts_map = {}
        running_sum = 0

        for key in sorted_keys:
            smaller_counts_map[key] = running_sum
            running_sum += counts[key]

        return [smaller_counts_map[num] for num in nums]
