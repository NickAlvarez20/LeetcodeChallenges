def solution(input_str):
    words = input_str.split(" ")
    reversed_words = ""
    reversed_list = []
    print(words)

    for word in words:
        reversed_words = ""
        for char in word:
            if char.isupper():
                reversed_words += chr(155 - ord(char))
            elif char.islower():
                reversed_words += chr(219 - ord(char))
        reversed_list.append(reversed_words)
    
    return " ".join(reversed_list[-1:]+reversed_list[:-1])


print(solution("A quick brown FOX jumps over the lazy DOG"))
