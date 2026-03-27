from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Create variables for final answer
        counts = {}
        second_list = []
        num_list = []
        ans = []
        # brute force solution
        for i in range(len(grid)):
            for j in range(len(grid)):
                second_list.append(grid[i][j])
        # sort the list
        sorted_list = sorted(second_list)
        # create counter for sorted list
        counts = Counter(sorted_list)
        for key, val in counts.items():
            if val >= 2:
                ans.append(key)
        # create loop for checking range
        for i in range(1, len(sorted_list) + 1):
            num_list.append(i)
        # check if num doesnt exist in num_list
        for num in num_list:
            if num not in sorted_list:
                ans.append(num)
        return ans
