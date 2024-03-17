#!/usr/bin/python3
""" Module for Lockboxes algorithm implementation """


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    keys = [0]
    number_of_boxes = len(boxes)
    for key in keys:
        for box_number in boxes[key]:
            if box_number not in keys and box_number < number_of_boxes:
                keys.append(box_number)

    return len(boxes) == len(keys)
