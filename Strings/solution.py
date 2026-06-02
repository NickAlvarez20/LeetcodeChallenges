def special_order(inputString):
    result = ""
    length = len(inputString)

    for i in range(length // 2 + length % 2):
        result += inputString[length - 1 - i]
    for i in range(length // 2 + length % 2):
        if length - 1 - i != i:
            result += inputString[i]
    return result


test = special_order("abcdefghijklmnopqrstuvwxyz" * 4 + "abcd")

print(test)
