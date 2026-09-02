class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l, r, r2 = m - 1, m+n-1, n - 1
        while r2 >= 0:
            if l >= 0 and nums1[l] > nums2[r2]:
                nums1[r] = nums1[l]
                l -= 1
            else:
                nums1[r] = nums2[r2]
                r2 -= 1
            r -= 1
        return nums1


test = [1,2,3,0,0,0] [1,2,3,2,5,6]
testTwo = [2,5,6]
Solution1 = Solution()
print(Solution1.merge(test, 3, testTwo, 3))

# Intuition:
# Ideally the intuition is to iterate through each array compare the values and then update pointers of the numbswan this involves keeping track of the nums 2 value and index using a 3rd pointer.
#
# Approach: 
# 1. We assign left right and right two pointers to the index position of M minus one right is assigned to N + N - 1 and R2 is assigned to N - 1
# 2. We create a while loop condition that says while the right pointer is greater than or equal to 0 which means that we have not exhausted the entire 2nd array
# 3. Then we conditionally check if the left pointer is greater than or equal to zero, And the value of the left pointer is greater than the value of the third pointer in the second array
# 3a. If this condition is true then we update the value of the current right pointer with the value of the current value of the left pointer 
# 3b. then we decrement the left pointer by one 
# #3c. then for every iteration we decrement the right pointer
# 4. Otherwise we update the value of the right pointer with the current value of the 3rd pointer in the 2nd array
# 4a. Then we decrement the 3rd pointer by one
# 4c. Then we universe the decrement the right pointer by one
# 5. Finally we return the sorted and merged array


# Time complexity: O(m+n)
# Time complexity Is O of M + N for the length of any given array plus the other array that we are merging with. 
# Space complexity: O(1)
# Space complexity is constant since we are updating in place and when not using any extra space

# Analysis: 
# The term complexity is zero milliseconds it beats 100% of solutions and the memory is 19.41 megabits it beats 16.05% of solutions.
# This one was a great challenge much tougher than easy problem and helped to expand awareness of a 3 pointer concept in addition to learning the 2 pointer concept. 


# Alternative Approach:
# 1. Using counter and updates to concurrently traverse and update any matches with 0 within first array, then set value equal to index position from 2nd array, then using sort
# class Solution:
# def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     counter = 0
#     # One initial pass to update the zero's
#     for i in range(0, len(nums1)):
#         if nums1[i] == 0 and counter < len(nums2):
#             nums1[i] = nums2[counter]
#             counter += 1
#     return nums1.sort()

# So the runtime is zero milliseconds it beats 100% of solutions and the memory is 19.40 megabytes beats 28.69% of solutions. This is actually not how you're supposed to solve it because of the zeros that are just placeholders but it works we just use the sort of the newly updated array and it sorts it and solves the problem.


# 2. Loop and replace with counter, then use bubble sort and swap to sort
# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         counter = 0
#         # One initial pass to update the zero's
#         for i in range(0, len(nums1)):
#             if nums1[i] == 0 and counter < len(nums2):
#                 nums1[i] = nums2[counter]
#                 counter += 1
#         for i in range(len(nums1)):
#             left, right = 0, 1
#             while left < len(nums1):
#                 if nums1[left] > nums1[right]:
#                     nums1[left], nums1[right] = nums1[right], nums1[left]
#                 left += 1
#                 right += 1
#         return nums1

# extra logic from problem solving
# if nums1[r] < nums2[r2]:
#                 nums1[r], nums2[r2] = nums2[r2], nums1[r]
#                 r2 -= 1
#                 if nums1[l] > nums1[r]:
#                     nums1[l], nums1[r] = nums1[r], nums1[l]
#                     l += 1
#                     r -= 1
#                 else:
#                     l += 1
#                     r -= 1
#         return nums1
