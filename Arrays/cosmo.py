def solution(numbers):
    n = len(numbers)
    result = []

    for i in range(n):
        # reverse the current elem, and store for later use
        reverse_elem = str(numbers[i])[::-1]
        int_reverse = int(reverse_elem)
        original_num = str(int_reverse)[::-1]
        original_num_int = int(original_num)

        # iterate through check if current elem has a reverse_elem, if not skip with pass
        if numbers[i] == original_num_int and int_reverse in numbers:
            result.append((numbers[i], int(reverse_elem)))
        elif int_reverse == original_num_int and int_reverse in numbers:
            result.append((numbers[i], int(reverse_elem)))
        else:
            pass
    return result


nums = [10, 1, 20, 2]


test_case = solution(nums)

print(test_case)
