class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        result = []
        for _ in range(n):
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1

        return result

# Intuition
# Utilize a two pointers approach set the first left pointer to zero and the right pointer equal to in this will allow us to traverse the entire list while updating a result list accordingly

# Approach
# It's necessary to use a left and right pointer approach with a new result variable that we will pin all the variables to in order to correct the shuffle the existing array properly we also use a for loop in range with the dummy variable and then append the left and the rig....ment by one and finally return result


# Complexity
# - Time complexity: O(N)
# The time complexity is linear because the loop executes exactly in times performing constant time insertions on each iteration 



# - Space complexity: O(N)
# The space complexity is O of N because the output array result scales linearly storing exactly 2n elements


# Code
# ```python3 []
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         left = 0
#         right = n
#         result = []
#         for _ in range(n):
#             result.append(nums[left])
#             result.append(nums[right])
#             left += 1
#             right += 1
            
#         return result