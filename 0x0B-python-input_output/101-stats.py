#!/usr/bin/python3
"""define module"""


import sys

total_f_size = 0
status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
        }
lines = 0

try:
    for line in sys.stdin:
        try:
            ip, _, date, _, status_code, file_size = line.split()
            file_size = int(file_size)

            total_f_size += file_size
            status_counts[int(status_code)] += 1

            lines += 1

            if lines % 10 = 0:
                print_statistics()
        except ValueError:
            pass
except KeyboardInterrupt:
    pass

print_statistics()

def print_statistics():
    print("Total file size:", total_f_size)
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")
