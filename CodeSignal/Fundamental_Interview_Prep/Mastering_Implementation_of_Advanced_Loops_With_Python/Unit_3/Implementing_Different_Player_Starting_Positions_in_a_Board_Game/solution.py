def solution(board, obstacle):
    # initialize an array of 0's for the length of the board
    moves = [0] * len(board)

    # iterate the board and grab the index, value and count total moves until we reach end of board or -1 if we hit an obstacle
    for index, value in enumerate(board):
        position = index
        count = 0
        while position < len(board):
            if board[position] == obstacle:
                moves[index] = -1
                break
            count += 1
            position += board[
                position
            ]  # grabs value at current position, this is used for the next index
        else:
            moves[index] = count

    return moves
