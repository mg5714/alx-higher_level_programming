#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("Number of argument(s): 0.")
    else:
        print("Number of argument(s): {}".format(count))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
