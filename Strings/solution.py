def reversed_triple_chars(s: str) -> str:
    result = ""
    for i in range(0, len(s), 3):
        curr_slice = s[i : i + 3]
        length = len(curr_slice)
        reverse_slice = curr_slice[::-1]
        if len(curr_slice) == 3:
            result += reverse_slice
        else:
            result += curr_slice
    return result


test = reversed_triple_chars("abcdef")

# outputs cbafed

print(test)
