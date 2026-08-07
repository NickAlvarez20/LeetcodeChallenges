def solution(listA, listB):
    # TODO: Find the pairs of integers a, b where a belongs to listA and b belongs to listB such that a is greater than b

    result = []

    for i in listA:
        for j in listB:
            if i > j:
                result.append((i, j))
                break
    return result


print(solution([5, 1, 8, -2, 0], [3, 2, 7, 10, -1]))
