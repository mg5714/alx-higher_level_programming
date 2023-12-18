#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print(int_value)
        return True
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return False
