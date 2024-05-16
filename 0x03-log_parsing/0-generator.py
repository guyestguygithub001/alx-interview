#!/usr/bin/python3
'''
This script is designed to generate random HTTP request logs.
'''
import random
import sys
import datetime
from time import sleep

# The script will generate 10,000 logs
for i in range(10000):
    # Introduce a random delay between each log
    sleep(random.random())
    # Write a formatted log entry to stdout
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
        # Generate a random IP address
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        # Use the current date and time
        datetime.datetime.now(),
        # Use a fixed request path
        '/projects/1216',
        # Use a fixed HTTP version
        'HTTP/1.1',
        # Randomly select a status code
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        # Randomly generate a file size
        random.randint(1, 1024)
    ))
    # Ensure the log entry is immediately written to stdout
    sys.stdout.flush()

