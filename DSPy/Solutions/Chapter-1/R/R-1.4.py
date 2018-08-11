#!/usr/bin/env python3

"""
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive
integers smaller than n.
"""

def sum_of_squares_less_than_n(n):
    """

    :param n: a positive integer
    :return:
    """
    sum = 0
    for i in range(1, n):
        sum += i*i
    return sum

print (sum_of_squares_less_than_n(2))
print (sum_of_squares_less_than_n(5))

