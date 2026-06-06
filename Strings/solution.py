def solution(s):
    groups = []
    curr_group_char = None
    curr_group_length = 0

    for char in s:
        if char == curr_group_char:
            curr_group_length += 1
        else:
            if curr_group_char is not None:
                groups.append((curr_group_char, curr_group_length))
            curr_group_char = char
            curr_group_length = 1

    if curr_group_char is not None:
        groups.append((curr_group_char, curr_group_length))

    groups.reverse()

    return groups


print(solution("aaabbcccdde"))
