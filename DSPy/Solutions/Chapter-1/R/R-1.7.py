#!/usr/bin/enb/python3
"""
Give a single command that computes the sum from Exercise R-1.6, rely- ing on Python’s comprehension syntax and
the built-in sum function
"""

def sum_of_squares_odds_less_than_n(n):

    return sum(i*i for i in range(n) if i%2!=0)

print (sum_of_squares_odds_less_than_n(5))
print (sum_of_squares_odds_less_than_n(6))