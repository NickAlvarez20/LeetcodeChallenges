def solution(numbers):
    middle = len(numbers) // 2  # middle index if odd, right = middle index if even

    if len(numbers) % 2 == 1:
        # init two pointers
        left = middle - 1
        right = middle + 1
        # establish middle points
        multiplied = [numbers[middle]]
    else:
        left = middle - 1
        right = middle
        multiplied = []

    # utilize a while loop to traverse and construct multiplied
    while left >= 0 and right < len(numbers):
        multiplied.append(numbers[left] * numbers[right])
        left -= 1
        right += 1

    return multiplied
