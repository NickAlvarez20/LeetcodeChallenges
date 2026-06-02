def special_order(inputString):
    result = ""  # init result
    length = len(inputString)  # grab length

    for i in range(length // 2 + length % 2):
        result += inputString[length - 1 - i]
    for i in range(length // 2 + length % 2):
        if length - 1 - i != i:
            result += inputString[i]
    return result


test = special_order("abcdefghijklmnopqrstuvwxyz" * 4 + "abcd")

print(test)
