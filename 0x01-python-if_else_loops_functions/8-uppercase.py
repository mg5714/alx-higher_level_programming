#!/usr/bin/python3

def uppercase(string):
    for char in string:
        c = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print(c, end="")
    print()
