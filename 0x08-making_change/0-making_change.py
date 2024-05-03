#!/usr/bin/python3
"""
Module for the makeChange function.
"""


def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet a given `total`
    """
    if total <= 0:
        return 0

    coin_count = 0
    coins.sort(reverse=True)

    for coin in coins:

        while total - coin >= 0:
            total -= coin
            coin_count += 1

        if total == 0:
            return coin_count

    return -1
