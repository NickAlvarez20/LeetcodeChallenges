def solution(num1, num2):
    # subtract num2 from num1 without int conversions
    num3 = 0

    i, j, borrow, num3 = len(num1) - 1, len(num2) - 1, 0, []

    while i >= 0 or j >= 0 or borrow > 0:
        n1 = int(num1[i] if i >= 0 else 0)
        n2 = int(num2[j] if j >= 0 else 0)
        total = n1 - n2 - borrow
        if total < 0:
            total = n1 + 10 - n2 - borrow
            borrow = 1
        else:
            borrow = 0
        curr = total % 10
        num3.append(str(curr))
        i, j = i - 1, j - 1

    result = "".join(num3[::-1]).lstrip("0")

    if result == "":
        return "0"
    else:
        return result
