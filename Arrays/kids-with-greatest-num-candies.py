class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest_val = max(candies)
        curr_sum = 0
        for kid in candies:
            curr_sum = kid + extraCandies
            if curr_sum >= greatest_val:
                result.append(True)
            else:
                result.append(False)
        return result
