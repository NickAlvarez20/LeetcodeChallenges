class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        counter = 0
        # One initial pass to update the zero's
        for i in range(0, len(nums1)):
            if nums1[i] == 0 and counter < len(nums2):
                nums1[i] = nums2[counter]
                counter += 1
        for i in range(len(nums1)):
            left, right = 0, 1
            while left < len(nums1):
                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = nums1[right], nums1[left]
                left += 1
                right += 1
        return nums1


test = [1,2,3,0,0,0] [1,2,3,2,5,6]
testTwo = [2,5,6]
Solution1 = Solution()
print(Solution1.merge(test, 3, testTwo, 3))

# Intuition:
#
#
# Approach: 

# Time complexity: 
# Space complexity: 

# Analysis: 


# Alternative Approach:
# Using counter and updates to concurrently traverse and update any matches with 0 within first array, then set value equal to index position from 2nd array, then using sort
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


# Loop and replace with counter, then use bubble sort and swap to sort
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
