def replace_substring(text, old, new):
    result_pieces = []
    current_index = 0
    start_pos = text.find(old)

    len_old = len(old)

    while start_pos != -1:
        result_pieces.append(text[current_index:start_pos]) # append the current up to start_pos index

        result_pieces.append(new) # append new word to replace old word

        current_index = start_pos + len_old # moves index to after the current word

        start_pos = text.find(old, current_index) # finds using old as keyword and starts searching from current index updated pos

    result_pieces.append(text[current_index:]) # appends everything that is after the last old word pos that is found
    return "".join(result_pieces)


replace_substring("hello world", "world", "friend")
