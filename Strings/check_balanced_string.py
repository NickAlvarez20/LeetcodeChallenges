class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_even = 0
        sum_odd = 0
        for index, val in enumerate(num):
            if index%2 == 0:
                sum_even += int(val)
            elif index%2 != 0:
                sum_odd += int(val)
        if sum_even != sum_odd:
            return False
        return True
        