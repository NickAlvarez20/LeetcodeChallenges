import math


def solution(arr1, arr2):

    curr_sum = 0
    result = list()

    for i in arr1:
        for j in arr2:
            curr_sum = i + j
            root = int(math.sqrt(abs(curr_sum)))
            if root * root == curr_sum:
                result.append((i, j))

    return result


arr1 = [100, 75, 36, 9, -25, -64, -100]
arr2 = [-1, 1, 24, 0, -1, -24]

print(solution(arr1, arr2))
