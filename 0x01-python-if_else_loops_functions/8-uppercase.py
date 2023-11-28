#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        if islower(c):
            c = chr(ord(c) - 32)
        print(c, end='')
    print()

