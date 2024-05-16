#!/usr/bin/python3
"""This script analyzes HTTP request logs to extract useful metrics."""

import re

def extract_input(input_line):
    """Parses a single line from an HTTP request log and extracts key information."""
    # Define the regular expression pattern for log line components
    fp = (
        r'\s*(?P<ip>\S+)\s*',  # IP address
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',  # Timestamp
        r'\s*"(?P<request>[^"]*)"\s*',  # Request string
        r'\s*(?P<status_code>\S+)',  # Status code
        r'\s*(?P<file_size>\d+)'  # File size
    )
    # Initialize default values for extracted information
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    # Combine the patterns into a full regular expression for log lines
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    # Match the regular expression with the input line
    resp_match = re.fullmatch(log_fmt, input_line)
    # If a match is found, extract the status code and file size
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info

def print_statistics(total_file_size, status_codes_stats):
    """Displays the aggregated statistics of file sizes and status codes from the log."""
    print('Total file size: {:d}'.format(total_file_size), flush=True)
    # Iterate through status codes and print non-zero counts
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('Status code {:s}: {:d} occurrences'.format(status_code, num), flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the running totals of file sizes and status code occurrences."""
    # Extract information from the current line
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    # Increment the count for the encountered status code
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    # Add the file size from the current line to the total
    return total_file_size + line_info['file_size']

def run():
    """Initiates the log parsing process."""
    line_num = 0
    total_file_size = 0
    # Initialize a dictionary to track occurrences of each status code
    status_codes_stats = {
        '200': 0,  # OK
        '301': 0,  # Moved Permanently
        '400': 0,  # Bad Request
        '401': 0,  # Unauthorized
        '403': 0,  # Forbidden
        '404': 0,  # Not Found
        '405': 0,  # Method Not Allowed
        '500': 0,  # Internal Server Error
    }
    try:
        # Continuously read lines until interrupted
        while True:
            line = input()
            # Update metrics with information from the current line
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            # Print statistics every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Print final statistics upon interruption or end of file
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
#!/usr/bin/python3
"""This script analyzes HTTP request logs to extract useful metrics."""

import re

def extract_input(input_line):
    """Parses a single line from an HTTP request log and extracts key information."""
    # Define the regular expression pattern for log line components
    fp = (
        r'\s*(?P<ip>\S+)\s*',  # IP address
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',  # Timestamp
        r'\s*"(?P<request>[^"]*)"\s*',  # Request string
        r'\s*(?P<status_code>\S+)',  # Status code
        r'\s*(?P<file_size>\d+)'  # File size
    )
    # Initialize default values for extracted information
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    # Combine the patterns into a full regular expression for log lines
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    # Match the regular expression with the input line
    resp_match = re.fullmatch(log_fmt, input_line)
    # If a match is found, extract the status code and file size
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info

def print_statistics(total_file_size, status_codes_stats):
    """Displays the aggregated statistics of file sizes and status codes from the log."""
    print('Total file size: {:d}'.format(total_file_size), flush=True)
    # Iterate through status codes and print non-zero counts
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('Status code {:s}: {:d} occurrences'.format(status_code, num), flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the running totals of file sizes and status code occurrences."""
    # Extract information from the current line
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    # Increment the count for the encountered status code
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    # Add the file size from the current line to the total
    return total_file_size + line_info['file_size']

def run():
    """Initiates the log parsing process."""
    line_num = 0
    total_file_size = 0
    # Initialize a dictionary to track occurrences of each status code
    status_codes_stats = {
        '200': 0,  # OK
        '301': 0,  # Moved Permanently
        '400': 0,  # Bad Request
        '401': 0,  # Unauthorized
        '403': 0,  # Forbidden
        '404': 0,  # Not Found
        '405': 0,  # Method Not Allowed
        '500': 0,  # Internal Server Error
    }
    try:
        # Continuously read lines until interrupted
        while True:
            line = input()
            # Update metrics with information from the current line
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            # Print statistics every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Print final statistics upon interruption or end of file
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
