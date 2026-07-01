def spot_swaps(source: str, target: str) -> list:
    result_arr = []
    i = 0

    while i < len(source) - 1:
        if (
            (source[i] != target[i])
            and source[i + 1] == target[i]
            and source[i] == target[i + 1]
        ):
            result_arr.append((i, source[i], target[i]))

            i += 2
        else:
            i += 1

    return result_arr


print(spot_swaps("hello", "hlelo"))
