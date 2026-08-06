class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        # create a set
        dict_nums = set(nums)

        while original in dict_nums:
            original = original * 2
        return original
