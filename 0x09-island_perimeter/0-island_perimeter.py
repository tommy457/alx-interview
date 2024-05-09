#!/usr/bin/python3
"""
Module for the island_perimeter function.
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """
    perimeter = 0
    row = len(grid)
    col = len(grid[0])

    if row == 0 or col == 0:
        return 0

    for row in range(row):
        for col in range(col):
            if grid[row][col] == 1:

                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter