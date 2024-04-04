#!/usr/bin/python3
"""
Module for the validUTF8 function.
"""


def validUTF8(data):
    """ check if data set represents a valid UTF-8 encoding. """

    i = 0
    while i < len(data):
        leading_byte: str = f"{data[i]:08b}"
        if leading_byte.startswith("0"):
            bytes = 1

        elif leading_byte.startswith("110"):
            bytes = 2

        elif leading_byte.startswith("1110"):
            bytes = 3

        elif leading_byte.startswith("11110"):
            bytes = 4

        else:
            return False

        if i + bytes > len(data):
            return False

        for j in range(1, bytes):
            if not f"{data[i + j]:08b}".startswith("10"):
                return False

        i += bytes

    return True
