#!/usr/bin/env python3

"""
Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m,
that is, n = mi for some integer i, and False otherwise.
"""


def is_multiple(n, m):
    try:
        if n%m==0:
            return True
    except ZeroDivisionError:
        if n == 0:
            return True
    return False

print (is_multiple(4,2))
print (is_multiple(2,3))
print (is_multiple(2,0))
print (is_multiple(0,0))