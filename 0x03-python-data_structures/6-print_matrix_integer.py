#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    idx = 1
    for i in matrix:
        for x in i:
            if idx < len(row) - 1:
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x), end="")
        print()
