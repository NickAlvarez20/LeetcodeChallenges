def solution(input_str):
    split_str = input_str.split()
    result = ''

    for word in split_str:
        if word[0].isalpha():
            word = word[0].upper() + word[1:].lower()
            result += word + " "
        else:
            word = word[0] + word[1:].lower()
            result += word + " "
        

    return "".join(result).rstrip()

print(solution("hello world"))
