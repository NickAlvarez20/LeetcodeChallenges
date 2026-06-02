def special_order(inputString):
    res = ""
    length = len(inputString)

    for i in range(length // 2 + length % 2):
        res += inputString[length - 1 - i]
    for i in range(length // 2 + length % 2):
        if length - 1 - i != i:
            res += inputString[i]

    return res


test = special_order("abcdefghijklmnopqrstuvwxyz" * 4 + "abcd")

print(test)
