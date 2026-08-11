def solution(sentence):
    # 1. Split the sentence
    words = sentence.split(" ")
    result = ""

    # 2. Check even length of the words in sentence
    for word in words:
        if len(word) % 2 == 1:
            for i in range(0, len(word), 2):
                result += word[i]
    return result[::-1]
