#!/usr/bin/python3
import sys

def print_solution(board):
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
            board[i] - i == row - col or \
            board[i] + i == row + col:
            return False
    return True

def solve_nqueens(board, col):
    n = len(board)
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(board, col + 1)

def check_args():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def main():
    n = check_args()
    board = [-1] * n
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()

