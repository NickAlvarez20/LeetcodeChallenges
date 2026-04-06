class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans_1 = []
        ans_2 = []
        for num in nums1:
            if num not in nums2 and num not in ans_1:
                ans_1.append(num)
        for num in nums2:
            if num not in nums1 and num not in ans_2:
                ans_2.append(num)
        return [ans_1, ans_2]
        