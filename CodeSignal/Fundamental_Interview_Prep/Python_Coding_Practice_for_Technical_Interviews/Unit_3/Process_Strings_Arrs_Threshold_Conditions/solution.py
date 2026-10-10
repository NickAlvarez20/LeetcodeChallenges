def solution(arr, text):
    sum_so_far = 0
    result = ""
    num_result = []
    i = 0

    while i < len(arr) and i < len(text) and sum_so_far < 30:
        if abs(arr[i] - 3) > 30:
            break
        else:
            sum_so_far += abs(arr[i] - 3)
            num_result.append(abs(arr[i] - 3))

        if sum_so_far > 30:
            sum_so_far -= abs(arr[i] - 3)
            num_result.pop()
            break

        if text[i].islower():
            result += chr((((ord(text[i]) - ord("a")) + 1) % 26) + ord("a"))
        else:
            result += text[i]
        i += 1

    return result, arr[i:]
