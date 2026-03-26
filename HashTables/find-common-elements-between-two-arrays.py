class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts_1, counts_2 = {}, {}

        # check if value in one exists in 2
        for num in nums1:
            if num in nums2:
                counts_1[num] = counts_1.get(num, 0) + 1

        for num in nums2:
            if num in nums1:
                counts_2[num] = counts_2.get(num, 0) + 1

        return [sum(counts_1.values()), sum(counts_2.values())] # returns sum of all values within dictionary
