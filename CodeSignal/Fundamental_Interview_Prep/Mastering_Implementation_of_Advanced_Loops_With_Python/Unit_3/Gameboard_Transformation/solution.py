def solution(numbers):
    # so look at the current value and check the range ahead, if the numbers within the range are equal to a negative number, replace the current value with the index value of the negative number, if the current value is negative, replace it with a -1. if no number ahead of the range is negative, keep the same number
    result = []

    for index, value in enumerate(numbers):
        position = index + 1  # starting position
        limit = index + value  # current_index + number of steps is the max limit
        found_obstacle = False  # boolean condition flag
        # guard clause
        if value < 0:
            result.append(-1)
            continue  # ensure it continues
        while position <= limit and position < len(numbers):  # boundary checks
            curr_value = numbers[position]
            if curr_value < 0:
                result.append(
                    position
                )  # Store the obstacle's position (index), not value
                found_obstacle = True
                break
            position += 1  # otherwise it continues
        if not found_obstacle:
            result.append(value)

    return result
