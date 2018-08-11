#!/usr/bin/env python3

"""
Give a single command that computes the sum from Exercise R-1.4,
rely- ing on Python’s comprehension syntax and the built-in sum function.
"""

def sum_of_squares_less_than_n_lst_comprehension(n):
    """

    :param n: a positive integer
    :return:
    """
    return sum(i*i for i in range(1,n))

print (sum_of_squares_less_than_n_lst_comprehension(2))
print (sum_of_squares_less_than_n_lst_comprehension(5))