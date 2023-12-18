#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print(int_value)
        return True
    except ValueError as err:
        print(f"Exception: {err}", file=sys.stderr)
        return False
