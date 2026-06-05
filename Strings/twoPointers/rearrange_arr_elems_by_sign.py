class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Pre allocate result arrow to save memory overhead
        res = [0] * len(nums)

        # Init two pointers
        pos_idx = 0
        neg_idx = 1

        # Single pass through the original array
        for num in nums:
            if num > 0:
                res[pos_idx] = num
                pos_idx += 2
            else:
                res[neg_idx] = num
                neg_idx += 2

        return res
        





# Uses two pointers, but incorrectly

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos_ints = []
#         neg_ints = []
#         res = []

#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 pos_ints.append(nums[i])

#         for j in range(len(nums)):
#             if nums[j] < 0:
#                 neg_ints.append(nums[j])

#         # double loop comparion and add
#         left = 0
#         right = 0

#         for i in range(len(pos_ints)):
#             res.append(pos_ints[left])
#             res.append(neg_ints[right])
#             left += 1
#             right += 1
#         return res
