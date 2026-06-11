def solution(input_string):
    result = ""
    i = 0

    while i < len(input_string):
        if input_string[i].isalpha():
            result += input_string[i]
            i += 1
        elif input_string[i].isdigit():
            num = ""
            while (
                i < len(input_string) and input_string[i].isdigit()
            ):  # collects the digits
                num += input_string[i]
                i += 1
            while i < len(input_string) and not input_string[i].isalpha():
                i += 1
            result += input_string[i]
            result += num
            i += 1
        else:
            result += input_string[i]
            i += 1
    return result


print(solution("I have 2 apples and 5 oranges and 3 grapefruits."))
