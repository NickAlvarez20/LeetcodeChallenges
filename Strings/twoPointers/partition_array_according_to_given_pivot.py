class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                ans[right] = nums[j]
                right -= 1

        while left <= right:
            ans[left] = pivot
            left += 1

        return ans


nums = [9, 12, 5, 10, 14, 3, 10]

test = Solution()

print(test.pivotArray(nums, 10))


# Straight-forward approach

# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         # rearrange the arr so nums to left of pivot are less than
#         less_than_result = []
#         equal_result = []
#         greater_than_result = []

#         for i in range(len(nums)):
#             if nums[i] < pivot:
#                 less_than_result.append(nums[i])
#         for i in range(len(nums)):
#             if nums[i] == pivot:
#                 equal_result.append(nums[i])
#         for i in range(len(nums)):
#             if nums[i] > pivot:
#                 greater_than_result.append(nums[i])

#         return less_than_result + equal_result + greater_than_result
