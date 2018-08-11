#!/usr/bin/env python3

"""
Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and
largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your
solution.
"""

def minmax(data):
    """

    :param data: a list or a sequence
    :return:a tuple min, max
    """
    if len(data) == 0:
        print ('min and max cannot be defined for null sequence')
        return
    else:
        max = min = data[0]
        for item in data:
            if item > max:
                max = item
            if item < min:
                min = item

    return min, max

print (minmax([2,1,5,4]))
print (minmax([]))