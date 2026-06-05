def unusual_traversal(arr):
    n, mid = len(arr), len(arr) // 2

    if n % 2 == 1:
        left = mid - 1
        right = mid + 1
        result = [arr[mid]]
    else:
        left = mid - 1
        right = mid
        result = []

    while left >= 0:
        if left - 1 >= 0:
            result.append(arr[left - 1])
        if left >= 0:
            result.append(arr[left])
        if right < n:
            result.append(arr[right])
        if right + 1 < n:
            result.append(arr[right + 1])

        left -= 2
        right += 2

    return result
