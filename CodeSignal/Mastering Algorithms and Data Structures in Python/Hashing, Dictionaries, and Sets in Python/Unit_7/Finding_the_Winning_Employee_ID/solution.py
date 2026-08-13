def elect_board_member(votes):
    count_dict = {}

    for vote in votes:
        count_dict[vote] = count_dict.get(vote, 0) + 1
        if count_dict[vote] > len(votes) // 3:
            return vote
    return -1


print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1
