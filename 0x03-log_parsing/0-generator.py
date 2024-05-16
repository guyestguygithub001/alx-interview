#!/usr/bin/python3
# This script generates random HTTP request logs.

import random
import sys
import datetime
from time import sleep

# Generate 10,000 logs.
for i in range(10000):
    # Pause for a random amount of time.
    sleep(random.random())

    # Write a log entry to standard output.
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
        random.randint(1, 255),  # Random IP address.
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        datetime.datetime.now(),  # Current date and time.
        '/projects/1216',  # Requested URL.
        'HTTP/1.1',  # HTTP version.
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Random status code.
        random.randint(1, 1024)  # Random file size.
    ))

    # Flush the output buffer to ensure the log entry is written immediately.
    sys.stdout.flush()

