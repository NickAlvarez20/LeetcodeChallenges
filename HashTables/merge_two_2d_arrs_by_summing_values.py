from collections import Counter


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        # Direct conversion to list from the merged Counter
        change_to_list = list((Counter(dict(nums1)) + Counter(dict(nums2))).items())

        # Sort in-place to avoid creating a second list copy
        change_to_list.sort()

        return change_to_list
