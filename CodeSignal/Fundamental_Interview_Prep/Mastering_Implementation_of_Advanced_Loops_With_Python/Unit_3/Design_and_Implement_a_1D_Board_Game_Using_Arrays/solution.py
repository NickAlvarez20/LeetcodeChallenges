def evaluatePath(numbers):
    position = 0
    moves = 0
    direction = 1
    changes = 0

    while True:
        jump = direction * numbers[position]
        new_position = position + jump

        # Check for blockade (0) or out of bounds
        if jump == 0 or new_position < 0 or new_position >= len(numbers):
            direction *= -1
            changes += 1
            if changes == 2:
                break
            continue
        else:
            position = new_position
            moves += 1
    return (position, moves)
