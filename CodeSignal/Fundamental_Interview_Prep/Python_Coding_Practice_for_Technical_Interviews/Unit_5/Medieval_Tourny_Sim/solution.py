def tournament(knights):
    rounds = 0

    while len(knights) != 1:
        winning_knights = []
        n = len(knights)
        total_strength = 0
        if len(set(knights)) == 1:
            return rounds
        if len(knights) <= 1:
            return rounds
        for i in range(len(knights)):
            total_strength = knights[i] - (knights[(i + 1) % n])
            if total_strength > 0:
                winning_knights.append(total_strength)
        if len(winning_knights) <= 0:
            return rounds
        if len(winning_knights) == len(knights):
            return rounds

        knights = winning_knights
        rounds += 1

    return rounds
