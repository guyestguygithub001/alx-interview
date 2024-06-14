#!/usr/bin/python3
"""
This module contains a function that rotates a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): The 2D matrix to rotate.

    Returns:
        None
    """
    # The matrix is square (n x n), so we only need one dimension size.
    n = len(matrix)

    # Perform a four-way swap for each layer, starting from the outermost layer and working inwards.
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            # Save the top element.
            top = matrix[first][i]
            # Move the left element to the top.
            matrix[first][i] = matrix[last - offset][first]
            # Move the bottom element to the left.
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move the right element to the bottom.
            matrix[last][last - offset] = matrix[i][last]
            # Move the saved top element to the right.
            matrix[i][last] = top
