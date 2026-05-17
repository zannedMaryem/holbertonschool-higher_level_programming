#!/usr/bin/python3
"""
This module provides a function that divides all elements
of a matrix by a number ensuring type safety by raising a
TypeError when inputs are not integers or floats.
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of
            integers/floats, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)

    return new_matrix
