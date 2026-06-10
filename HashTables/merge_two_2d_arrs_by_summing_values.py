from collections import Counter


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        # create 2 counters
        nums1_count = Counter()
        nums2_count = Counter()

        for index, val in enumerate(nums1):
            nums1_count[val[0]] = val[1]

        for index, val in enumerate(nums2):
            nums2_count[val[0]] = val[1]

        total_count = nums1_count + nums2_count

        change_to_list = list(total_count.items())
        change_to_list.sort()

        return change_to_list
