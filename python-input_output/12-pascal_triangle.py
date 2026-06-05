#!/usr/bin/python3
"""This module defines a function to generate Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n
    
    Args:
        n: An integer representing the number of rows
        
    Returns:
        A list of lists of integers representing Pascal's triangle
        Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    
    return triangle
