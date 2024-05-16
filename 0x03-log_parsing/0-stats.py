#!/usr/bin/python3
import sys
import signal

def print_stats(status_codes, file_size):
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats(status_codes, file_size)
    sys.exit(0)

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            parts = line.split()
            size = int(parts[-1])
            code = parts[-2]
            if code in status_codes:
                status_codes[code] += 1
            file_size += size
        except:
            pass
        if i % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt:
    pass
finally:
    print_stats(status_codes, file_size)
