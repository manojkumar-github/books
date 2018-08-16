#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as
­ppp p v = v1 +v2 +···+vn.
 For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the
 vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of
 √42 + 32 = √16 + 9 = √25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
  value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
"""


def norm(v,p=2):
    """

    :param v: a list of numbers
    :param p:
    :return: p norm value of 'v'
    """
    sum = 0
    for item in v:
        sum += item**p
    return sum**(1/p)

print (norm([1,2,3])) # eucliden norm with default p=2
print (norm([1,2,9,10], p=4))
