def solution(arrayA, arrayB, arrayC):
    max_valueB = 0
    max_valueC = 0
    indexA = 0
    indexB = None
    indexC = None
    visited = set()
    curr_step = 0

    while True:
        if curr_step == 0:  # hops to B
            indexB = arrayA[indexA]  # grab next hop
            if indexB >= len(arrayB):
                break
            if (indexB, "A") in visited:
                break
            else:
                visited.add((indexB, "A"))

            if arrayB[indexB] > max_valueB:
                max_valueB = arrayB[indexB]

            curr_step += 1
        elif curr_step == 1:  # hops to A
            indexA = arrayB[indexB]
            if indexA >= len(arrayA):
                break
            if (indexA, "B") in visited:
                break
            else:
                visited.add((indexA, "B"))

            curr_step += 1
        elif curr_step == 2:  # hops to C
            indexC = arrayA[indexA]
            if indexC >= len(arrayC):
                break
            if (indexC, "C") in visited:
                break
            if arrayC[indexC] > max_valueC:
                max_valueC = arrayC[indexC]
            visited.add((indexC, "A"))

            curr_step += 1
        elif curr_step == 3:  # hops to A
            indexA = arrayC[indexC]
            if indexA >= len(arrayA):
                break
            if (indexA, "C") in visited:
                break
            else:
                visited.add((indexA, "C"))
            curr_step = 0

    return max_valueB + max_valueC
