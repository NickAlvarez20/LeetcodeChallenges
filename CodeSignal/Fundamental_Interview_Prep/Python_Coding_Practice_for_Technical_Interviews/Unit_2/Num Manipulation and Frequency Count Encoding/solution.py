from collections import Counter


def solution(numbers):
    result = []
    # loop through and do conditions checks
    for i in range(len(numbers)):
        if numbers[i] % 10 == 0:
            numbers[i] = 1
        elif numbers[i] % 10 != 0:
            numbers[i] += 1

    freq_dict = Counter(numbers)

    for key, val in freq_dict.items():
        result.append(val * key)

    return sorted(result)
