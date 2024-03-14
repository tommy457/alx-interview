#!/usr/bin/python3
""" Module for Lockboxes algorithm implementation """


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    keys = set()
    for box in boxes:
        try:
            keys.add(box[0])
        except Exception:
            pass

    for box_number in range(1, len(boxes)):
        if box_number not in keys:
            return False
    return True
