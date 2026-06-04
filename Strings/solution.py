def solution(numbers):
    # Create an array with tuple, counting from the middle, account for odd and even length based, if odd append with a 0
    mid = len(numbers) // 2

    # conditionals
    if len(numbers) % 2 == 1:
        # pointers
        left = mid - 1
        right = mid + 1
        tuple_list = [(numbers[mid], 0)]  # set middle element
    else:
        left = mid - 1
        right = mid
        tuple_list = []  # blank

    while left >= 0 and right < len(numbers):

        tuple_list.append((numbers[left], numbers[right]))
        print(tuple_list)
        left -= 1
        right += 1
    return tuple_list


test = solution([1, 2, 3, 4, 5])

print(test)
