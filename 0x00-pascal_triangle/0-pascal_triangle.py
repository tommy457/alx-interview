#!/usr/bin/python3
"""Module for Pascal’s triangle Algorithm implementation"""


def pascal_triangle(n):
    """Create list of lists of integers representing the Pascal’s triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            new_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    new_row.append(1)
                else:
                    new_row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            triangle.append(new_row)

    return triangle
