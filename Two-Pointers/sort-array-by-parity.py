# # Intuition
# Using a two-pointer approach, we can check the left and right values and swap any if the left is equal to an odd number and the right is equal to an even number.

# # Approach
# 1. Declare two variables left and right. Set left equal to 0 and right equal to the length of the nums array minus 1.
# 2. Initialize a while loop for the condition left is less than right.
# 3. Check if the current value within the left index position within the numbers array modulus 2 is equal to 0. If so, we can pass and increment the left  pointer by 1.
# 4. else if the number's right pointer value modulus 2 is odd we can pass and decrement by 1
# 5. Otherwise, we want to swap the left and right with the right and left because this indicates that we have found an odd on the left and an even on the right. So we want it to go from evens on the left side of the array to odds on the right side. Then we want to increment left by one and decrement right pointer by one.
# 6. We can finally return the numbers array and it will have sorted it in place.


# # Complexity
# - Time complexity: The time complexity is O(n).
# We have a while loop and we check conditions. Each of these checks within our loop runs for the entire length of the nums resulting in O of n time complexity. And a simple swap is also O of 1.

# - Space complexity: The space complexity is O(1), constant auxiliary space.
# We declare left and right, which assign minimal space. Then, we are sorting in place using the left and right two-pointers approach. Therefore, we do not allocate any extra auxiliary memory. Therefore, O(1) constant auxiliary space.

# Code

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                pass
                left += 1
            elif nums[right] % 2 == 1:
                pass
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

                
            
            
        return nums
