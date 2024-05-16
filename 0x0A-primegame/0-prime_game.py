#!/usr/bin/python3
"""
Module for the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n """
    sieve = [True for _ in range(n + 1)]
    prime = []

    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """ Returns the winner of Prime Game """
    if x <= 0 or not nums:
        return None

    maria = 0
    ben = 0

    for i in range(x):
        prime = primes(nums[i])

        if len(prime) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return 'Maria'

    if ben > maria:
        return 'Ben'
    return None
