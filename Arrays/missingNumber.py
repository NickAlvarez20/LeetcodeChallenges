class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(0, len(nums) + 1):
            if i not in nums:
                ans = i
        return ans


# # Time Complexity - O(n^2)
# The time complexity is O of N squared because the algorithm uses a loop that runs in plus one times and inside the loop it performs an O of inserts operation on the input list therefore if we combine these considering the for loop and the inside for if condition that's n*n so that's N ^2

# Space Complexity - O(1)
# Space complexity algorithm only uses a fixed amount of additional memory for simple variables answer and I regardless of how large the input list grows
