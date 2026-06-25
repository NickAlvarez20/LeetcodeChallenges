class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for item in nums:
            split_num = str(item)
            for char in split_num:
                result.append(int(char))
        return result
