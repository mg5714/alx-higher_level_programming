#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    int_value = int(value)
    try:
        print("{:d}".format(int_value))
        return True
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return False
