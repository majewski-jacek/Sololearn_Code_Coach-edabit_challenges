def bingo_check(board):
    index_bingo = []
    
    for horizontal_bingo in board:
        if 'x' not in horizontal_bingo:
            continue

        # checks diagonals bingo
        elif len(set(horizontal_bingo)) == 1:
            return True

        else:
            index_bingo.append(horizontal_bingo.index('x'))
    
    # checks vertical bingo
    if len(set(index_bingo)) == 1:
        return True

    # checks diagonals bingo
    elif index_bingo == [0, 1, 2, 3, 4] or index_bingo == [4, 3, 2, 1, 0]:
        return True

    return False


# https://edabit.com/challenge/mJpjpgxkxvTY4Qbwf