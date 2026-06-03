class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result = []
        if len(matrix) < 1:
            result.append(0)
        for elem in matrix:
            result.append(sum(elem))
        return result
