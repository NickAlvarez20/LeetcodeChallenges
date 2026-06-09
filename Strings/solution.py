def solution(s):
    split_str = s.split("-")
    result =[]

    for char in split_str:
        if char.isalpha():
            result.append(str(ord((char))-96)) # turns a-> 1
        elif char.isdigit():
            result.append(str(chr(96+int(char)))) # turns 1 -> a
    return "-".join(result)


print(solution("a-b-c-1-2-3-x-y-z-24-25-26"))
