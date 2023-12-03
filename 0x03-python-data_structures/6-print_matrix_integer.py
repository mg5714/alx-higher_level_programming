#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        idx = 1
        for x in i:
            if idx == len(i):
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x), end="")
        print()
