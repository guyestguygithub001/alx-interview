#!/usr/bin/python3

"""
This module provides a function to validate UTF-8 encoded data.
"""

def validUTF8(data):
    """
    Checks if a list of integers represents valid UTF-8 codepoints.

    This function follows the UTF-8 encoding rules specified in RFC 3629
    (https://datatracker.ietf.org/doc/html/rfc3629#page-4).

    Args:
        data (list): A list of integers representing the byte values.

    Returns:
        bool: True if the input data is valid UTF-8, False otherwise.
    """
    skip = 0
    n = len(data)

    for i in range(n):
        # Skip continuation bytes
        if skip > 0:
            skip -= 1
            continue

        # Check for invalid byte values
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 0x10ffff:
            return False

        # Handle 1-byte characters
        elif data[i] <= 0x7f:
            skip = 0

        # Handle 4-byte UTF-8 characters
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span:
                next_body = [x & 0b11000000 == 0b10000000 for x in data[i + 1: i + span]]
                if all(next_body):
                    skip = span - 1
                else:
                    return False
            else:
                return False

        # Handle 3-byte UTF-8 characters
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span:
                next_body = [x & 0b11000000 == 0b10000000 for x in data[i + 1: i + span]]
                if all(next_body):
                    skip = span - 1
                else:
                    return False
            else:
                return False

        # Handle 2-byte UTF-8 characters
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span:
                next_body = [x & 0b11000000 == 0b10000000 for x in data[i + 1: i + span]]
                if all(next_body):
                    skip = span - 1
                else:
                    return False
            else:
                return False

        # Invalid byte sequence
        else:
            return False

    return True

