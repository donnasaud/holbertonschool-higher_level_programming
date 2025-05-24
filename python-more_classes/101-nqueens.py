#!/usr/bin/python3
"""Solves the N Queens problem."""

import sys


def print_usage_and_exit(msg, code=1):
    """Print a message and exit with the given status code."""
    print(msg)
    sys.exit(code)


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions."""
    def backtrack(row, board):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)

    board = [-1] * n
    backtrack(0, board)


# ---- Main program starts here ----
if len(sys.argv) != 2:
    print_usage_and_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except ValueError:
    print_usage_and_exit("N must be a number")

if N < 4:
    print_usage_and_exit("N must be at least 4")

solve_nqueens(N)
