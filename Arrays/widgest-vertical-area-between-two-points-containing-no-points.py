class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = []
        for elem in points:
            x_points.append(elem[0])

        sorted_points = sorted(x_points)

        max_dist = 0
        n = len(sorted_points)

        for index, val in enumerate(range(n - 1)):
            curr_dist = sorted_points[index + 1] - sorted_points[index]
            max_dist = max(max_dist, curr_dist)

        return max_dist
