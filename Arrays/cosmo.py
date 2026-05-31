import math


def solution(n):
    result = 0
    curr_class = int(math.log10(n) + 1)
    # get rid of trailing 0's
    while n > 0:
        digit = n % 10  # grabs last digit
        curr_class = int(math.log10(n))
        if digit == 0:
            pass
        else:
            result += digit * math.pow(10, curr_class)
        n = n // 10  # removes last digit
    return int(result)
