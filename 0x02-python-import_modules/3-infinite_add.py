#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0
    for i in range(1, len(sys.argv)):
        temp = int(sys.argv[i])
        result += temp
    print(f"{result}")
