#!/usr/bin/python3
# This is a module for rotating a 2D matrix.

def rotate_2d_matrix(matrix):
    # This function rotates a 2D matrix in place.
    
    # Return if the matrix is not a list or is empty.
    if type(matrix) != list or len(matrix) <= 0:
        return
    
    # Return if any element in the matrix is not a list.
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Return if any row in the matrix has a different length.
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    
    c, r = 0, rows - 1  # Initialize column and row indices.
    
    # Iterate over all elements in the matrix.
    for i in range(cols * rows):
        # Start a new row in the rotated matrix.
        if i % rows == 0:
            matrix.append([])
        
        # Reset row index and increment column index after a full cycle.
        if r == -1:
            r = rows - 1
            c += 1
        
        # Append the current element to the last row of the rotated matrix.
        matrix[-1].append(matrix[r][c])
        
        # Remove the original row after all its elements have been appended.
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        
        r -= 1  # Move to the next element in the current column.
