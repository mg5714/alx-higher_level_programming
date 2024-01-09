#!/usr/bin/python3
"""define module"""

from sys import stdin


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
total_f_size = 0


def print_statistics():
    """"to print"""
    print(f"Total file size: {total_f_size}")
    for k, v in sorted(status_counts):
        if v > 0:
            print("{:s}: {:d}".format(k, v))

try:
    for line in stdin:
            file_split = line.split()
            if len(file_split) >= 2:
                status_code = file_split[-2]
                total_f_size += int(file_split[-1])
                if status_code in status_counts:
                    status_counts[(status_code)] += 1

            lines += 1

            if lines % 10 == 0:
                print_statistics()
    print_statistics()

except KeyboardInterrupt as e:
    print_statistics()
