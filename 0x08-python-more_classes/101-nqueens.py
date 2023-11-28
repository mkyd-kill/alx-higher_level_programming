#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)
    if not solutions:
        print("No solution exists")
    else:
        for solution in solutions:
            print(solution)

def solve_util(board, col, N, solutions):
    if col >= N:
        sol = []
        for i in range(N):
            row = [i, board[i].index(1)]
            sol.append(row)
        solutions.append(sol)
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            if solve_util(board, col + 1, N, solutions):
                continue

            board[i][col] = 0

    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_n_queens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()

