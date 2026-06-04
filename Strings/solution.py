def solution(numbers):
    mid = len(numbers) // 2

    if len(numbers) % 2 == 1:
        left = mid-1
        right = mid+1
        list_tuples = [(numbers[mid], 0)]
    else:
        left = mid-1
        right = mid
        list_tuples = []

    while left >= 0 and right < len(numbers):
        list_tuples.append((numbers[left], numbers[right]))
        left -= 1
        right += 1
    return list_tuples


test = solution([1, 2, 3, 4, 5])

print(test)
