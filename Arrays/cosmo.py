import math


def solution(n):
    new_num = 0
    curr_power_count = 1
    first_num = n

    while n > 0:
        if n == first_num:
            digit = n % 10
            curr_val = digit * 11
            new_num = curr_val
            curr_power_count += 1
            n = n // 10
        else:
            digit = n % 10
            curr_val = digit * 11  # 33
            curr_pow = math.pow(10, curr_power_count)
            new_num += curr_val * curr_pow
            curr_power_count += 2
            n = n // 10

    return int(new_num)
