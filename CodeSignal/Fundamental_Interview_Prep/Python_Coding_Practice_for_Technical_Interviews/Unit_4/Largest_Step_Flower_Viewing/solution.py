def largest_step(garden, start, direction):
    jump = 1
    total_types = len(set(garden))
    largest_working_jump = -1

    if total_types == 1:
        return 1

    while (direction * jump) + start >= 0 and (direction * jump) + start < len(garden):
        visited_flowers = set()
        pos = start
        while 0 <= pos < len(garden):
            visited_flowers.add(garden[pos])
            pos += jump * direction

        if len(visited_flowers) == total_types:
            largest_working_jump = jump

        jump += 1

    return largest_working_jump
