#!/usr/bin/python3
import sys
if __name__ == "__main__":

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument.")
    else:
        print("{} argument:".format(count))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
