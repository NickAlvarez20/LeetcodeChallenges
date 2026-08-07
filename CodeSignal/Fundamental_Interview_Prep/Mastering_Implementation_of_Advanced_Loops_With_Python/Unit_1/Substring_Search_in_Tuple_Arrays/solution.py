def stringSearch(sourceArray, searchArray):
    # so looking at the tuple, we have to first compare the values in both index position 0
    # then if value of tuple in source array is less than or equal to value in search array and substring check exists, we can output to new list

    # First we need a result array to return output
    result = []

    for i in sourceArray:
        for j in searchArray:
            if i[0] <= j[0] and i[1] in j[1]:
                result.append(i)
                break
    return result


sourceArray = [(1, "abc"), (2, "def"), (3, "xyz")]
searchArray = [(1, "abcdef"), (5, "uvwxy")]

print(stringSearch(sourceArray, searchArray))
