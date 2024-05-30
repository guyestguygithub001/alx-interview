#!/usr/bin/python3
"""
This script solves the N-Queens Puzzle.
"""
import sys


def is_safe(board, row, col, n):
    """
    Determines if a queen can be safely placed at the given board position.
    """
    # Examine the row on the left side for any existing queens
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Examine the upper left diagonal for any existing queens
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Examine the lower left diagonal for any existing queens
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Uses backtracking to find all safe queen placements.
    """
    # If all queens are placed successfully, print the solution
    if col == n:
        print_solution(board, n)
        return

    # Try placing a queen in each row of the current column
    for i in range(n):

        if is_safe(board, i, col, n):
            # Place a queen at the current position
            board[i][col] = 1

            # Recursively place the rest of the queens
            solve_nqueens(board, col + 1, n)

            # If placing a queen here doesn't lead to a solution, remove it
            board[i][col] = 0


def print_solution(board, n):
    """
    Outputs the solution in the form of a chessboard.
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    """
    The main function of the script.
    """
    # Ensure the user provided the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0 for j in range(n)] for i in range(n)]

    # Start solving the N-Queens puzzle
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()

