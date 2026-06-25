from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # create freq arr
        freq_dict = Counter(nums)

        for key, val in freq_dict.items():
            if val % 2 != 0:
                return False
        return True
