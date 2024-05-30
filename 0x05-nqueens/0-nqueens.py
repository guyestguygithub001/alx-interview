#!/usr/bin/python3
"""
This module implements a solution to the N-Queens puzzle.

The N-Queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. A solution involves placing N queens on the board such that
no two queens can attack each other, i.e., they cannot be on the same row,
column, or diagonal.

This module provides functions to solve the N-Queens puzzle using a
backtracking algorithm and print all valid solutions.
"""


def is_safe(board, row, col, n):
    """
    Check if a queen can be safely placed at the given position on the board.

    Args:
        board (list): A 2D list representing the chessboard.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.
        n (int): The size of the chessboard (N×N).

    Returns:
        bool: True if it is safe to place a queen at the given position,
              False otherwise.
    """
    # Check if there is a queen in the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower-left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """
    Solve the N-Queens puzzle using backtracking.

    Args:
        board (list): A 2D list representing the chessboard.
        col (int): The current column index to place a queen.
        n (int): The size of the chessboard (N×N).
    """
    # Base case: If all queens are placed, print the solution
    if col == n:
        print_solution(board, n)
        return

    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen at the current position
            board[i][col] = 1

            # Recur to place the remaining queens
            solve_nqueens(board, col + 1, n)

            # If placing the queen in the current position doesn't lead to
            # a solution, remove the queen and backtrack
            board[i][col] = 0


def print_solution(board, n):
    """
    Print a solution to the N-Queens puzzle.

    Args:
        board (list): A 2D list representing the chessboard with a valid solution.
        n (int): The size of the chessboard (N×N).
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    """
    Entry point of the program.

    This function validates the command-line argument, initializes the chessboard,
    and calls the function to solve the N-Queens puzzle.
    """
    # Check if the user provided the correct number of arguments
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
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Call the function to solve the N-Queens puzzle
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
