def solution(s):
    removed_chars = []
    split_str = list(s)

    while len(split_str) != 0:
        curr_tuple_list = []
        n = len(split_str)
        if len(split_str) == 1:
            removed_chars.append(split_str[0])
            break
        for i in range(0, len(split_str), 2):
            if i + 1 < len(split_str):
                smallest_lexo = min(ord(split_str[i]), ord(split_str[(i + 1) % n]))
                largest_lexo = max(ord(split_str[i]), ord(split_str[(i + 1) % n]))
                if split_str[i] == split_str[i + 1]:
                    removed_chars.append(split_str[i])
                    curr_tuple_list.append(split_str[i + 1])
                else:
                    removed_chars.append(chr(smallest_lexo))
                    curr_tuple_list.append(chr(largest_lexo))
            else:
                curr_tuple_list.append(split_str[i])

        split_str = curr_tuple_list
        
    return removed_chars


