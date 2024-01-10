#!/usr/bin/python3
"""Module for matrix_mul"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or if any element is not an integer or float.
        ValueError: If m_a or m_b is empty or if matrices can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a must be a list of lists of integers/floats")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b must be a list of lists of integers/floats")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]


    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
