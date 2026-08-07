def common_elements(listA, listB):

    result = []

    for i in listA:
        for j in listB:
            if i in listB:
                result.append(i)
                break

    return result


print(common_elements([7, 2, 3, 9, 1], [2, 3, 7, 6]))
