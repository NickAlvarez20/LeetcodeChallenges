class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for letters in str(num):
                digit_sum += int(letters)

        return abs(elem_sum - digit_sum)

# Optimal Solution:


# class Solution:
#     def differenceOfSum(self, nums: List[int]) -> int:
#         elem_sum = sum(nums)
#         digit_sum = 0

#         for num in nums:
#             # Peel off digits using pure math
#             while num > 0:
#                 digit_sum += num % 10  # Grabs the last digit (e.g., 15 % 10 = 5)
#                 num = num // 10  # Chops off the last digit (e.g., 15 // 10 = 1)

#         return abs(elem_sum - digit_sum)


# # Intuition
# The problem asks for the absolute difference between the element sum and the digit sum of an array. The element sum is just the total of all numbers. The digit sum requires breaking each number down into its individual digits and adding them up. Since the element sum will always be greater than or equal to the digit sum, we can simply subtract the digit sum from the element sum.

# # Approach
# 1. Calculate the total sum of all integers in the array using the built-in `sum()` function.
# 2. Iterate through each number in the array to calculate the digit sum.
# 3. Convert each number to a string to easily access its individual character digits.
# 4. Convert each character back to an integer and add it to a running digit sum total.
# 5. Return the absolute difference between the element sum and the digit sum.

# # Complexity
# - Time complexity:
# \[O(n \times m)\]
# where n is the number of elements in the array and m is the maximum number of digits in a number.

# - Space complexity:
# \[O(m)\]
# to store the string representation of the numbers during conversion.

# # Code
# ```python3 []
# class Solution:
#     def differenceOfSum(self, nums: List[int]) -> int:
#         elem_sum = sum(nums)
#         digit_sum = 0
#         for num in nums:
#             for letters in str(num):
#                 digit_sum += int(letters)

#         return abs(elem_sum - digit_sum)
# ```
