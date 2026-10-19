def house_game(houses):

    # find max length of largest num in houses
    max_length = len(str(max(abs(x) for x in houses)))

    i = 1

    while i < max_length + 1:
        digit_index = i
        n = len(houses)
        new_houses = []
        stripped_digits = []
        updated_houses = []
        for j in range(len(houses)):
            # Guard Clause: check length of curr
            if len(str(houses[j])) < i:
                new_houses.append(str(houses[j]))
                stripped_digits.append("")
            else:
                # Step 1: Look at current value and strip the current index from far right
                num_to_add = (houses[j] % 10**digit_index) // 10 ** (digit_index - 1)
                stripped_digits.append(str(num_to_add))
                # Step 2: Strip value
                if i == 1:
                    temp = str(houses[(j) % n])
                    temp = str(int(temp) // 10)
                    if temp == "0":
                        new_houses.append("")
                    else:
                        new_houses.append(temp)
                else:
                    temp = str(houses[(j) % n])
                    temp = temp[:-i] + temp[-i + 1 :]
                    new_houses.append(temp)
        for k in range(len(stripped_digits)):
            new_num = stripped_digits[(k - 1) % n] + new_houses[k]
            updated_houses.append(int(new_num))

        if updated_houses == houses:
            break
        houses = updated_houses

        i += 1

    return houses

# Complete Fundamental Coding Interview Prep with Python Algorithm Certification