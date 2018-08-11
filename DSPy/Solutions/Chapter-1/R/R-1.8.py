#!/usr/bin/env/python3

"""
Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and
expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?
"""

"""
Ans: Consider a list s = [1,2,3,4,5,6] with positive indices and length n=6
If the indices are of -n <= k < 0 the indices would be -6,-5,-4,-3,-2,-1 whose actual indices in a normal list are
0,1,2,3,4,5.

By mapping the above indices set, we can estimate: for j>=0, s[2] = s[-4] or s[-3] = s[4]

Hence, s[j] = s[j-n]
"""