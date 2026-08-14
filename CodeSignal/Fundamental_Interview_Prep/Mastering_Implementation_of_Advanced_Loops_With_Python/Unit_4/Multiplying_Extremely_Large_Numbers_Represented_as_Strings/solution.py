def solution(num1, num2):
    result = [0] * (len(num1) + len(num2))
    carry = 0

    for i in range(len(num2) - 1, -1, -1):
        for j in range(len(num1) - 1, -1, -1):
            product = int(num2[i]) * int(num1[j])
            result[
                i + j + 1
            ] += product  # add to the end of result, updating the very right position
            result[i + j] += (
                result[i + j + 1] // 10
            )  # updates right position with ones positon
            result[i + j + 1] %= 10  # updates left position with tens position

    stringified = [str(digit) for digit in result]

    final_value = "".join(stringified).lstrip("0")

    if final_value == "":
        return "0"
    else:
        return final_value
