def solution(array1, array2):

    if array1 == array2:
        return (array1, 0)

    best_candidate = (float("inf"), float("inf"), [])
    i = 0

    while i >= 0 and i < len(array1):
        rotate_arr = array1[i:] + array1[:i]

        curr_manhattan_dist = 0
        for j in range(len(rotate_arr)):
            # calculate the current manhattan_dist
            curr_manhattan_dist += abs(rotate_arr[j] - array2[j])
        concat_int = int("".join(map(str, rotate_arr)))
        current_candidate = (curr_manhattan_dist, concat_int, rotate_arr)
        if current_candidate < best_candidate:
            best_candidate = current_candidate
        i += 1

    return (best_candidate[2], best_candidate[0])
