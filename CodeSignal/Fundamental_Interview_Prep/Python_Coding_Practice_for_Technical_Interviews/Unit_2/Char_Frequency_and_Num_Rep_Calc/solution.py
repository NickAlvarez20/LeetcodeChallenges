from collections import Counter


def solution(s):
    # returns a dict
    result_dict = dict()
    # string needs to be converted to array
    arr_str = list(s)  # [a,b,c]
    count_chars = Counter(arr_str)

    for char in arr_str:
        if ord(char) - 3 < 97:
            reduce_by = ord(char) % 97
            if reduce_by == 0:
                curr_char = 122 - 2
            elif reduce_by == 2:
                curr_char = 122
            else:
                curr_char = 122 - reduce_by
            result_dict[char] = int(count_chars[char]) * curr_char
        else:
            curr_char = ord(char) - 3
            result_dict[char] = int(count_chars[char]) * curr_char

    return {k: result_dict[k] for k in sorted(result_dict.keys())}
