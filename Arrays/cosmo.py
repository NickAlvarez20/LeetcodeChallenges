def solution(n):
    count = 0
    curr_digit = 0

    # remove the digit, check the curr digit, increase if matches, else continue

    while n > 0:
        digit = n % 10  # grab digit from end

        curr_digit = digit # set curr_digit = digit 4
        n = n // 10 # remove the digit  remove 4

        second_digit = n % 10 # 2

        if curr_digit == second_digit:
            count += 1
        elif curr_digit != second_digit:
            pass
    return count
