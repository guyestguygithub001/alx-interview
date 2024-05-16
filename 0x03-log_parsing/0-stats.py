#!/usr/bin/python3
# This script parses HTTP request logs.

import re

def extract_input(input_line):
    # This function extracts parts of an HTTP request log line.

    # Define the format of the log line.
    fp = (
        r'\s*(?P<ip>\S+)\s*',  # IP address
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',  # Date
        r'\s*"(?P<request>[^"]*)"\s*',  # Request
        r'\s*(?P<status_code>\S+)',  # Status code
        r'\s*(?P<file_size>\d+)'  # File size
    )

    # Initialize the information to be extracted.
    info = {
        'status_code': 0,
        'file_size': 0,
    }

    # Combine the format parts into a single regular expression.
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])

    # Match the input line against the format.
    resp_match = re.fullmatch(log_fmt, input_line)

    # If a match is found, extract the status code and file size.
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size

    return info

def print_statistics(total_file_size, status_codes_stats):
    # This function prints the total file size and status code statistics.

    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    # This function updates the total file size and status code statistics
    # based on a given log line.

    # Extract the information from the line.
    line_info = extract_input(line)

    # Update the status code statistics.
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1

    # Update the total file size.
    return total_file_size + line_info['file_size']

def run():
    # This function starts the log parser.

    # Initialize the line counter, total file size, and status code statistics.
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }

    try:
        # Continuously read lines of input.
        while True:
            line = input()

            # Update the metrics based on the current line.
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )

            # Increment the line counter.
            line_num += 1

            # Print the statistics every 10 lines.
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # If input ends, print the final statistics.
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()

