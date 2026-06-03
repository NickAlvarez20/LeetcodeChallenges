class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        reversed_arr = nums[::-1]
        return nums + reversed_arr
