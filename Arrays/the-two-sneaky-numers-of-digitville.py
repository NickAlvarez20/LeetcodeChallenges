from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        freq_dict = Counter(nums)
        for key, value in freq_dict.items():
            if value == 2:
                ans.append(key)
        return ans
