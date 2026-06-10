def solution(s):
    numbers = []
    num = ""

    for char in s:  # loops
        if char.isdigit():
            num += char
        elif num:
            numbers.append(int(num))
            num = ""
    if num:
        numbers.append(int(num))
    return sum(numbers)


print(
    solution(
        "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"
    )
)
