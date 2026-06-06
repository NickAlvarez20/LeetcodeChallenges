def solution(s):
    group = []
    curr_chars_in_group = None
    curr_chars_count = 0
    res = ''

    for index in range(0, len(s), 2):
        curr_block = s[index:index+2]
        if curr_block == curr_chars_in_group:
            curr_chars_count += 1
        else:
            if curr_chars_in_group is not None:
                group.append((curr_chars_in_group, curr_chars_count))
            curr_chars_in_group = curr_block
            curr_chars_count = 1
    if curr_chars_in_group is not None:
        group.append((curr_chars_in_group, curr_chars_count))


    for char, length in group:
        res += f"{char}{length}"

    return res

    


print(solution("aaababbababaca"))
