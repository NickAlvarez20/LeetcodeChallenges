def solution(n):
    num_odds = 0
    digit_product = 1
    while n > 0:
        digit = n % 10
        # if odd, increment num_odds and multiply
        if digit % 2 == 1:
            num_odds += 1
            digit_product *= digit
        elif digit % 2 == 0:
            pass
        n = n // 10
    if num_odds == 0:
        return 0
    else:
        return digit_product

