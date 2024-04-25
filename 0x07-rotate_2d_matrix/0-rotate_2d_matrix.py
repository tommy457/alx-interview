#!/usr/bin/python3
"""
Module for the rotate_2d_matrix function.
"""


def rotate_2d_matrix(matrix):
    """ rotate a NxN matrix 90 degrees clockwise in-place."""
    rows = len(matrix)

    # Transpose the matrix.
    for i in range(rows):

        for j in range(i, rows):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    # Reverce all rows
    for i in range(rows):
        matrix[i] = matrix[i][::-1]
