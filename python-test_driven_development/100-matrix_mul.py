#!/usr/bin/python3
"""Matrix multiplication with full input validation.

This module defines `matrix_mul(m_a, m_b)` which multiplies two matrices
after validating types, shapes, and contents, following the task’s rules.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b after strict validation.

    Args:
        m_a (list of lists of int/float): Left matrix.
        m_b (list of lists of int/float): Right matrix.

    Returns:
        list of lists of int/float: The product matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists,
                   or if elements are not int/float,
                   or if rows are not all the same size.
        ValueError: If m_a or m_b is empty, or if they cannot be multiplied.
    """
    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Validate elements are int/float
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate all rows are the same size
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplicability: columns in A == rows in B
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform multiplication
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            new_row.append(sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b))))
        result.append(new_row)

    return result
