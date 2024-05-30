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
    main()


Curriculum
Short Specializations
Average: 121.48%
0x05. N Queens
Algorithm
Python
 Weight: 1
 Project will start May 27, 2024 6:00 AM, must end by May 31, 2024 6:00 AM
 Checker was released at May 28, 2024 6:00 AM
 An auto review will be launched at the deadline
The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

Concepts Needed:
Backtracking Algorithms:

Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
Backtracking Introduction
Recursion:

Using recursive functions to implement backtracking algorithms.
Recursion in Python
List Manipulations in Python:

Creating and manipulating lists, especially to store the positions of queens on the board.
Python Lists
Python Command Line Arguments:

Handling command-line arguments with the sys module.
Command Line Arguments in Python
By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

Additional Resources
Mock Interview
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
Tasks
0. N queens
mandatory

Chess grandmaster Judit Polgár, the strongest female chess player of all time


The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking

julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
Repo:

GitHub repository: alx-interview
Directory: 0x05-nqueens
File: 0-nqueens.py
 
Copyright © 2024 ALX, All rights reserved.:::
