def encode_rle(s):
    groups = []
    curr_group_char = None
    curr_group_len = 0
    res = ""

    for char in s:
        if char.isalnum():
            if char == curr_group_char:
                curr_group_len += 1
            else:
                if curr_group_char is not None:
                    groups.append((curr_group_char, curr_group_len))
                curr_group_char = char
                curr_group_len = 1

    if curr_group_char is not None:
        groups.append((curr_group_char, curr_group_len))

    for char, length in groups:
        res += f"{char}{length}"

    return res


print(encode_rle("aaa@@bb!!c#d**e"))
