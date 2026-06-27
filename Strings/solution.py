def replace_substring(text, old, new):
    result_pieces = []
    current_index = 0
    len_old = len(old)

    start_pos = text.find(old)

    while start_pos != -1:
        result_pieces.append(text[current_index:start_pos])

        result_pieces.append(new)

        current_index = start_pos + len_old

        start_pos = text.find(old, current_index)
    result_pieces.append(text[current_index:])

    return "".join(result_pieces)


replace_substring("hello world", "world", "friend")
