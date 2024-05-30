#!/usr/bin/python3
"""
This module implements a solution finder for the N-Queens problem.

The N-Queens problem is a classic problem in computer science that involves placing
N queens on an N×N chessboard such that no two queens can attack each other. A queen
can attack any piece on the same row, column, or diagonal.

The module provides functions to retrieve user input, check for attacking positions
between queens, build solutions, and print the solutions.
"""

import sys

solutions = []
"""
The list of possible solutions to the N-Queens problem.
Each solution is represented as a list of tuples, where each tuple represents
the position of a queen on the chessboard.
"""

n = 0
"""
The size of the chessboard (N×N).
"""

pos = None
"""
A list of all possible positions on the chessboard, represented as tuples
(row, column).
"""

def get_input():
    """
    Retrieves and validates the program's argument (N) from the command line.

    Returns:
        int: The size of the chessboard (N).

    Raises:
        SystemExit: If the input is invalid or N is less than 4.
    """
    global n
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
    return n

def is_attacking(pos0, pos1):
    """
    Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (tuple): The position of the first queen (row, column).
        pos1 (tuple): The position of the second queen (row, column).

    Returns:
        bool: True if the queens are in an attacking position, False otherwise.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

def group_exists(group):
    """
    Checks if a group of positions (representing a solution) exists in the list of solutions.

    Args:
        group (list): A group of positions (tuples) representing a potential solution.

    Returns:
        bool: True if the group exists in the list of solutions, False otherwise.
    """
    for solution in solutions:
        if len(group) == len(solution) and all(pos in solution for pos in group):
            return True
    return False

def build_solution(row, group):
    """
    Recursively builds a solution for the N-Queens problem.

    Args:
        row (int): The current row on the chessboard.
        group (list): The current group of positions representing a potential solution.
    """
    global solutions, n
    if row == n:
        # Base case: All queens have been placed
        if not group_exists(group):
            solutions.append(group.copy())
    else:
        for col in range(n):
            # Try placing a queen in the current row and column
            position = (row, col)
            if all(not is_attacking(position, pos) for pos in group):
                # If the new position is not attacking any existing queens
                group.append(position)
                build_solution(row + 1, group)
                group.pop()

def get_solutions():
    """
    Generates and stores all possible solutions for the given chessboard size.
    """
    global pos, n
    pos = [(row, col) for row in range(n) for col in range(n)]
    build_solution(0, [])

def main():
    """
    Main entry point of the program.
    """
    global n, solutions
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()#!/usr/bin/python3
"""
This module implements a solution finder for the N-Queens problem.

The N-Queens problem is a classic problem in computer science that involves placing
N queens on an N×N chessboard such that no two queens can attack each other. A queen
can attack any piece on the same row, column, or diagonal.

The module provides functions to retrieve user input, check for attacking positions
between queens, build solutions, and print the solutions.
"""

import sys

solutions = []
"""
The list of possible solutions to the N-Queens problem.
Each solution is represented as a list of tuples, where each tuple represents
the position of a queen on the chessboard.
"""

n = 0
"""
The size of the chessboard (N×N).
"""

pos = None
"""
A list of all possible positions on the chessboard, represented as tuples
(row, column).
"""

def get_input():
    """
    Retrieves and validates the program's argument (N) from the command line.

    Returns:
        int: The size of the chessboard (N).

    Raises:
        SystemExit: If the input is invalid or N is less than 4.
    """
    global n
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
    return n

def is_attacking(pos0, pos1):
    """
    Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (tuple): The position of the first queen (row, column).
        pos1 (tuple): The position of the second queen (row, column).

    Returns:
        bool: True if the queens are in an attacking position, False otherwise.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

def group_exists(group):
    """
    Checks if a group of positions (representing a solution) exists in the list of solutions.

    Args:
        group (list): A group of positions (tuples) representing a potential solution.

    Returns:
        bool: True if the group exists in the list of solutions, False otherwise.
    """
    for solution in solutions:
        if len(group) == len(solution) and all(pos in solution for pos in group):
            return True
    return False

def build_solution(row, group):
    """
    Recursively builds a solution for the N-Queens problem.

    Args:
        row (int): The current row on the chessboard.
        group (list): The current group of positions representing a potential solution.
    """
    global solutions, n
    if row == n:
        # Base case: All queens have been placed
        if not group_exists(group):
            solutions.append(group.copy())
    else:
        for col in range(n):
            # Try placing a queen in the current row and column
            position = (row, col)
            if all(not is_attacking(position, pos) for pos in group):
                # If the new position is not attacking any existing queens
                group.append(position)
                build_solution(row + 1, group)
                group.pop()

def get_solutions():
    """
    Generates and stores all possible solutions for the given chessboard size.
    """
    global pos, n
    pos = [(row, col) for row in range(n) for col in range(n)]
    build_solution(0, [])

def main():
    """
    Main entry point of the program.
    """
    global n, solutions
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
