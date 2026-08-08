def solution(sentence, c):
    # so iterate through each word in sentence and find out if it is even. then split it, and check the letters in the second half. if they are less than target letter, concatenate to new string

    result_str = ""
    words = sentence.split(" ")

    for word in words:
        if len(word) % 2 == 0:
            mid = len(word) // 2
            split_word = word[mid:]
            for char in split_word:
                if ord(char) < ord(c):
                    result_str += char
    return result_str



print(solution("Python is a high-level programming language.", 'n'))