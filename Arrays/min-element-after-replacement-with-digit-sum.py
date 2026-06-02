class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for element in nums:
            element = str(element)
            elem_sum = 0
            for digit in element:
                elem_sum += int(digit)
            result.append(elem_sum)
        return min(result)
