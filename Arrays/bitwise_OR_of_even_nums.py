class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = []
        result = 0
        for num in nums:
            if num % 2 == 0:
                res.append(num)
        for i in range(len(res)):
            result |= res[i]
        return result


# # Intuition
# The problem requires finding the cumulative bitwise OR of all even numbers in a given list. My first thought was to isolate the even numbers first because odd numbers contain a 1 in their least significant bit, which would skew the bitwise OR result if included. Once the even numbers are isolated, accumulating them using the bitwise OR (|) operator yields the final answer.

# # Approach
# 1. Initialize an empty list res to hold the even numbers, and an integer result set to 0 to accumulate the bitwise OR.
# 2. Iterate through the input list nums. For each element, check if it is even using the modulo operator (num % 2 == 0). If it is even, append it to res.
# 3. Iterate through the res list using its indices and sequentially apply the bitwise OR assignment operator (|=) to combine all the even numbers into result.
# 4. Return the final accumulated result.

# # Complexity
# - Time complexity: O(n)
# We iterate through the input list nums of size n exactly once to filter the even numbers, and then iterate through the filtered list res (which has a maximum size of n) exactly once to compute the bitwise OR.

# - Space complexity: O(n)
# In the worst-case scenario where all numbers in the input list are even, the res list will store all n elements, requiring linear extra space.

# # Code
# class Solution:
#     def evenNumberBitwiseORs(self, nums: List[int]) -> int:
#         res = []
#         result = 0
#         for num in nums:
#             if num % 2 == 0:
#                 res.append(num)
#         for i in range(len(res)):
#             result |= res[i]
#         return result
