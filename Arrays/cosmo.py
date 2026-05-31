import math


def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        square_root = round(math.sqrt((numbers[i] * numbers[n - i - 1])), 2)
        result.append((numbers[i], square_root))
    return result
