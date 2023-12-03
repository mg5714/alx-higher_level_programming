#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, x in enumerate(i):
            if idx < len(i) - 1:
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x), end="")
        print()
