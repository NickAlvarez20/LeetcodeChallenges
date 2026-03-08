from collections import Counter


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        # Declare vars for length for loop
        n = len(nums)
        if n < k:
            return 0

        window_counts = Counter(nums[:k])
        curr_sum = sum(nums[:k])
        max_sum = 0

        if len(window_counts) == k:
            max_sum = curr_sum

        for i in range(k, n):
            new_val = nums[i]
            curr_sum += new_val
            window_counts[new_val] += 1

            # remove old element (leaving from left)
            old_val = nums[i - k]
            curr_sum -= old_val
            window_counts[old_val] -= 1
            if window_counts[old_val] == 0:
                del window_counts[old_val]

            if len(window_counts) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum
