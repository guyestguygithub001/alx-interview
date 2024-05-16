#!/usr/bin/python3
# This Python script simulates the generation of random HTTP request logs.

import random
import datetime
import sys
from time import sleep

# Loop to create 10,000 simulated log entries
for i in range(10000):
    # Introduce a random delay between log entries
    sleep(random.random())
    # Write a formatted log entry with a random IP, current timestamp, fixed URL, HTTP version, random status code, and random response size
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
        random.randint(1, 255),  # Randomly generated IP address segment
        random.randint(1, 255),  # Randomly generated IP address segment
        random.randint(1, 255),  # Randomly generated IP address segment
        random.randint(1, 255),  # Randomly generated IP address segment
        datetime.datetime.now(),  # Current timestamp
        '/projects/1216',         # Fixed URL path
        'HTTP/1.1',               # HTTP version
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Random HTTP status code
        random.randint(1, 1024)   # Random response size in bytes
    ))
    # Ensure the log entry is immediately written to stdout
    sys.stdout.flush()
