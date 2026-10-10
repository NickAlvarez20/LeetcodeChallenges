def solution(inputString, numbers):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    sum_so_far = 0
    result = ""
    i = 0

    while i < len(inputString) and i < len(numbers) and sum_so_far <= 100:
        if inputString[i] in vowels:
            result += "a" if inputString[i] == "u" else vowels[vowels.index(inputString[i])+1]
        elif inputString[i] in consonants:
            result += (
                "b" if inputString[i] == "z" else consonants[consonants.index(inputString[i])+1]
            )
        sum_so_far += numbers[i] * 3
        i += 1

    if sum_so_far < 100:
        return result, numbers[i:]
    else:
        return result, numbers[i:]


input_string = "example"
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(input_string, array))