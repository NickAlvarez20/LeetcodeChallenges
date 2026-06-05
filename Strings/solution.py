def unusual_traversal(array):
    mid = len(array) // 2

    if len(array) % 2 == 1:
        mutated_arr = [array[mid]]
        left = mid - 1
        right = mid + 1
    else:
        mutated_arr = []
        left = mid - 1
        right = mid

    while left >= 0 or right < len(array):
        if left - 1 >= 0:
            mutated_arr.append(array[left - 1])
        if left >= 0:
            mutated_arr.append(array[left])
        if right < len(array):
            mutated_arr.append(array[right])
        if right + 1 < len(array):
            mutated_arr.append(array[right + 1])

        left -= 2
        right += 2

    return mutated_arr
