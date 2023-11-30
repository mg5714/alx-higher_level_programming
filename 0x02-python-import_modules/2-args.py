#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument.")
    else:
        print("{} argument:".format(count))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
