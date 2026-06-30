class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        found = False
        # use OR operator to brute force
        for num in nums:
            for x in range(num):
                if (x | (x + 1)) == num:
                    found = True
                    ans.append(x)
                    break
            else:
                ans.append(-1)
        return ans


# Optimal solution 
# class Solution:
#     def minBitwiseArray(self, nums: List[int]) -> List[int]:
#         ans = []

#         for num in nums:
#             if num % 2 == 0:
#                 ans.append(-1)
#                 continue

#             temp = num
#             count = 0
#             while (temp & 1) == 1:
#                 count += 1
#                 temp = temp >> 1

#             ans.append(num - (1 << (count - 1)))
#         return ans


# # Intuition
# The problem requires finding the smallest integer x for each element in the input list such that applying a bitwise OR between x and x + 1 yields the original number. My first thought was to use a brute-force approach. Since the target number itself is relatively small or we need the smallest possible valid x, we can check every non-negative integer starting from 0 up to the number itself to see if it satisfies the bitwise condition.

# # Approach
# 1. Initialize an empty list ans to store the resulting integers for each element in nums.
# 2. Loop through each target integer num in the nums list.
# 3. For each num, run a nested loop using range(num) to test every possible candidate integer x from 0 up to num - 1.
# 4. Check if the condition (x | (x + 1)) == num evaluates to True.
# 5. If a matching x is found, append it to ans and break out of the inner loop immediately to ensure we keep the smallest valid integer.
# 6. Use an else block tied to the inner loop; if the loop finishes without finding any valid x, append -1 to ans.
# 7. Return the completed ans list.

# # Complexity
# - Time complexity: O(n * m)
# Where n is the number of elements in the nums list, and m is the average value of the numbers in nums. In the worst-case scenario, the inner loop runs num times for each element.

# - Space complexity: O(1)
# Excluding the output list ans which is required by the problem, the algorithm only uses a few primitive variables (like x and found) for tracking, requiring constant extra space.

# # Code
# class Solution:
#     def minBitwiseArray(self, nums: List[int]) -> List[int]:
#         ans = []
#         found = False
#         # use OR operator to brute force
#         for num in nums:
#             for x in range(num):
#                 if (x | (x+1)) == num:
#                     found = True
#                     ans.append(x)
#                     break
#             else:
#                 ans.append(-1)
#         return ans
