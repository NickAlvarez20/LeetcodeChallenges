def solution(strings, numbers):
    vowels = "aeiou"
    result = ""
    sum_so_far = 0
    i = 0

    while i < len(strings) and sum_so_far <= 100:
        if strings[i] in vowels:
            break
        result += chr((ord(strings[i]) - (ord("a")) - 1) % 26 + ord("a"))
        sum_so_far += abs(numbers[i]) * 2
        i += 1

    return result, numbers[i:]
