def encode_rle(s):
    groups = []
    current_group_char = None
    current_group_length = 0
    res = ''

    for char in s:
        if char.isalnum():
            if char == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    groups.append((current_group_char, current_group_length))
                current_group_char = char
                current_group_length = 1
    if current_group_char is not None:
        groups.append((current_group_char, current_group_length))

    for char, length in groups:
        res += f"{char}{length}"

    return res



print(encode_rle("aaa@@bb!!c#d**e"))
