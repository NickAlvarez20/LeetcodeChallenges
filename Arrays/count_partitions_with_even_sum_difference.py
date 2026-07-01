class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        curr_index = 1
        count = 0
        for i in range(len(nums) - 1):
            slice1 = nums[0:curr_index]
            slice2 = nums[curr_index:]
            arr_sum = sum(slice1) - sum(slice2)
            if arr_sum % 2 == 0:
                count += 1
            curr_index += 1
        return count


# # optimal solution
# class Solution:
#     def countPartitions(self, nums: List[int]) -> int:
#         # If the total sum is even, all splits are even. Otherwise, none are.
#         return len(nums) - 1 if sum(nums) % 2 == 0 else 0

# # Intuition
# The problem asks us to find how many split points create two subarrays where the difference of their sums is even. Mathematically, `Sum(Left) - Sum(Right) = Sum(Total) - 2 * Sum(Right)`. Because subtracting any multiple of 2 always preserves the original parity, the parity of the difference depends entirely on the total sum of the array. If the total sum is even, every partition will have an even difference. If it is odd, no partition will.

# # Approach
# Instead of looping through the array, slicing elements, and calculating sums repeatedly, we can find the answer in a single mathematical check:
# 1. Calculate the total sum of the array.
# 2. Check if the total sum is even (`total_sum % 2 == 0`).
# 3. If it is even, all possible `n - 1` split points are valid. Return `len(nums) - 1`.
# 4. If it is odd, no split points are valid. Return `0`.

# # Complexity
# - Time complexity:
# \[O(n)\]
# — We only iterate through the array once to compute the total sum using the built-in `sum()` function.

# - Space complexity:
# \[O(1)\]
# — No extra arrays, slices, or data structures are created, using constant memory.

# # Code
# ```python3 []
# class Solution:
#     def countPartitions(self, nums: List[int]) -> int:
#         # If the total sum is even, all splits are valid. Otherwise, none are.
#         return len(nums) - 1 if sum(nums) % 2 == 0 else 0
# ```

