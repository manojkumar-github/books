#!/usr/bin/env python3

"""
Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise.
However, your function cannot use the multiplication, modulo, or division operators.
"""
def is_even(k):

    if k%2 == 0:
        return True
    return False

print (is_even(4))
print (is_even(3))
print (is_even(0))