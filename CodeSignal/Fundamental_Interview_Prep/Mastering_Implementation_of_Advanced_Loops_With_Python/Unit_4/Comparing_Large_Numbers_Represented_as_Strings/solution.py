def solution(num1, num2):

    if len(num1) > len(num2):
        return 1
    if len(num2) > len(num1):
        return -1
    if len(num1) == len(num2):
        for i in range(len(num1)):
            if num1[i].zfill(10) > num2[i].zfill(10):
                return 1
            elif num2[i].zfill(10) > num1[i].zfill(10):
                return -1
    return 0
