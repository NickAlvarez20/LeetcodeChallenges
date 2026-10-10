def solution(dungeon, health):
    x = 1
    max_found = dict()

    while x >= 0 and x <= len(dungeon):
        pos = 0
        current_health = health
        while 0 <= pos < len(dungeon):
            current_health -= dungeon[pos]
            if current_health <= 0:
                break
            pos += x
        if current_health > 0:
            max_found[x] = current_health
        x += 1

    return max(max_found, key=max_found.get) if max_found else 0
