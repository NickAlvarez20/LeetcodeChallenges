from collections import Counter


def solution(sentence):
    result = ""
    words = sentence.split(" ")

    for index, word in enumerate(words):
        if len(word) % 2 == 1:

            freq_dict_word = Counter(word.lower())
            counts = list(freq_dict_word.values())
            test_val = counts[0]

            all_equal = True
            for ele in freq_dict_word:
                if freq_dict_word[ele] != test_val:
                    all_equal = False
                    break

            if all_equal:
                result += word[0].lower()
            else:
                most_common_char = max(freq_dict_word, key=freq_dict_word.get)
                result += most_common_char

    return result


print(solution("nested loops"))
