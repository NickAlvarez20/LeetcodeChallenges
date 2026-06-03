class Solution(object):
    def findLHS(self, nums):
        # sort the nums array for determining subsequence
        sorted_arr = sorted(nums)
        L = 0
        if len(sorted_arr) == 0:
            return 0
        for R in range(len(sorted_arr)):
            while (sorted_arr[R] - sorted_arr[L]) > 1:
                L += 1
            if sorted_arr[R] - sorted_arr[L] == 1:
                length = R-L+1
                res = max(res, length)
        return res


test_one = Solution()
nums_arr = [1, 3, 2, 2, 5, 2, 3, 7]
test_one.findLHS(nums_arr)
