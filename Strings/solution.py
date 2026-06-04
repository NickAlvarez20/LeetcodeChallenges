def solution(numbers):
    mid = len(numbers) // 2

    if len(numbers) % 2 == 1:
        left = mid-1
        right = mid+1
        list_tups = [(numbers[mid], 0)]
    else:
        left = mid-1
        right = mid
        list_tups = []

    while left >= 0 and right < len(numbers):
        list_tups.append((numbers[left], numbers[right]))

        left -= 1
        right += 1

    return list_tups


test = solution([1, 2, 3, 4, 5])

print(test)
