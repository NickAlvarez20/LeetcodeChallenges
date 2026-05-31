import math


def solution(numbers):
    n = len(numbers)  # len of original arr
    result = []  # for determining pairs
    result_two = []  # for sums of pairs
    slice_len = 0  # determine the slice length
    # grab the pairs
    for i in range(n):
        result.append([numbers[i], numbers[n - i - 1]])

    slice_len = math.ceil(len(result) / 2)  # accounts for odd and even arrs
    sliced_result = result[
        0:slice_len:1
    ]  # slice and store the array of pairs up to a certain point
    len_new_arr = len(sliced_result)  # len of new sliced result
    # sum the pairs and output to new result arr
    for i in range(len_new_arr):
        result_two.append(sum(sliced_result[i]))
    return result_two
