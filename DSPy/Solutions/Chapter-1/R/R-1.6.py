#!/usr/bin/env python3
"""
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd
positive integers smaller than n.
"""

def sum_of_squares_odds_less_than_n(n):

    return sum(i*i for i in range(n) if i%2!=0)

print (sum_of_squares_odds_less_than_n(5))
print (sum_of_squares_odds_less_than_n(6))