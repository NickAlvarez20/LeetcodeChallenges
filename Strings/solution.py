def solution(numbers):
    mid = len(numbers) // 2

    if len(numbers) % 2 == 1:
        left = mid-1
        right = mid + 1
        tuple_list = [(numbers[mid], 0)]
    else:
        left = mid - 1
        right = mid
        tuple_list = []
    
    while left >= 0 and right < len(numbers):
        tuple_list.append((numbers[left], numbers[right]))
        left -= 1
        right += 1
        print(tuple_list)

    return tuple_list


test = solution([1, 2, 3, 4, 5])

print(test)
