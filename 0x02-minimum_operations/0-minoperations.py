#!/usr/bin/python3
"""
Module for the minOperations function
"""


def minOperations(n: int) -> int:
    """Returns the fewest number of operations
    required to reach n starting from 1.
    """
    min_operations: int = 0
    divisor: int = 2
    while n > 1:
        while n % divisor == 0:
            min_operations += divisor
            n /= divisor
        divisor += 1
    return min_operations
