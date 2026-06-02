# so after a we update the next position with d, which is 3 chars to the left of a


def repeat_char_jump(inputString, k):
    result = str(inputString[0])  # init first char
    length = len(inputString)
    current_index = 0

    while len(result) < length:
        current_index = (current_index + k) % length
        result += inputString[current_index]

    return result


test = repeat_char_jump("abcdefghij", 9)
print(test)
