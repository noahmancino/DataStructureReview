'''
This took me about an hour to write. It runs in six minutes on my machine for n=9
'''

import copy
def is_valid(board):
    occupied_squares = []
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square == 'Q':
                occupied_squares.append((i, j))

    for i, cord1 in enumerate(occupied_squares):
        for cord2 in occupied_squares[i+1:]:
            # check straight lines
            if cord1[0] == cord2[0] or cord2[1] == cord1[1]:
                return False
            # check diagonals
            if abs(cord1[1] - cord2[1]) == abs(cord1[0] - cord2[0]):
                return False
    return True


def n_queens_helper(board, n, invalid_cords):
    if n == 0:
        return [board]

    solutions = []
    new_invalid_cords = invalid_cords[:]
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square != 'Q' and (i, j) not in invalid_cords:
                new_invalid_cords.append((i, j))
                new_board = copy.deepcopy(board)
                new_board[i][j] = 'Q'
                if is_valid(new_board):
                    solutions += n_queens_helper(new_board, n - 1, new_invalid_cords)

    return solutions


def n_queens(n):
    row = ['*' for _ in range(n)]
    board = [row[:] for _ in range(n)]
    solutions = []
    invalid_cords = []
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            new_board = copy.deepcopy(board)
            new_board[i][j] = 'Q'
            invalid_cords.append((i, j))
            solutions += n_queens_helper(new_board, n - 1, invalid_cords)

    return solutions

for i, sol in enumerate(n_queens(9)):
    print(i)
    print(sol)
