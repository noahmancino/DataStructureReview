'''
This took me about an hour to write. It runs in about 1 minute and 40 seconds on my machine.
This was a case were I finished a semi-naive solution (backtracking) and realized I needed to optimize it.
I didn't have to think hard to find optimizations, but every time I would finish on an optimization I realized
that there was a better way to do it. The backtracking could always check one row at a time, but I was too
lazy to implement that.
'''
import copy


def is_valid(occupied_squares):
    occupied_squares = list(occupied_squares)
    for i, cord1 in enumerate(occupied_squares):
        for cord2 in occupied_squares[i+1:]:
            # check straight lines
            if cord1[0] == cord2[0] or cord2[1] == cord1[1]:
                return False
            # check diagonals
            if abs(cord1[1] - cord2[1]) == abs(cord1[0] - cord2[0]):
                return False
    return True


def n_queens_helper(board, n, invalid_cords, occupied_squares):
    if n == 0:
        return [board]

    solutions = []
    new_invalid_cords = invalid_cords[:]
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            new_occupied = copy.copy(occupied_squares)
            new_occupied.add((i, j))
            new_invalid_cords.append((i, j))
            if (i, j) not in invalid_cords and is_valid(new_occupied):
                new_board = copy.deepcopy(board)
                new_board[i][j] = 'Q'
                solutions += n_queens_helper(new_board, n - 1, new_invalid_cords, new_occupied)

    return solutions


def n_queens(n):
    row = ['*' for _ in range(n)]
    board = [row[:] for _ in range(n)]
    solutions = []
    invalid_cords = []
    row = board[0]
    for j, square in enumerate(row):
        new_board = copy.deepcopy(board)
        new_board[0][j] = 'Q'
        invalid_cords.append((0, j))
        solutions += n_queens_helper(new_board, n - 1, invalid_cords, {(0, j)})

    return solutions

for i, sol in enumerate(n_queens(9)):
    print(i)
    print(sol)