#!/usr/bin/python3
"""define function"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                cu_row = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(cu_row)

    return triangle
