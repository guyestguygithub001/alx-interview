#!/usr/bin/python3
"""
This script solves the minimum operations coding challenge.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations required to obtain exactly n 'H' characters.
    """
    # Validate input: only proceed if n is an integer
    if not isinstance(n, int):
        return 0

    ops_count = 0  # Initialize the operations counter
    clipboard = 0  # Initialize the clipboard content
    done = 1       # Start with one 'H' character on the screen

    # Loop until we have the desired number of 'H' characters
    while done < n:
        # If the clipboard is empty, perform the initial copy-paste operation
        if clipboard == 0:
            clipboard = done  # Copy all 'H' characters from the screen
            done += clipboard  # Paste the 'H' characters to double the count
            ops_count += 2  # Increment the operations count for copy and paste

        # If the remaining 'H' characters needed is a multiple of the current count
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done  # Copy all 'H' characters from the screen
            done += clipboard  # Paste to add the copied 'H' characters
            ops_count += 2  # Increment the operations count for copy and paste

        # If there are 'H' characters in the clipboard, paste them
        elif clipboard > 0:
            done += clipboard  # Paste the 'H' characters to increase the count
            ops_count += 1  # Increment the operations count for paste

    # Return the total number of operations performed
    return ops_count
