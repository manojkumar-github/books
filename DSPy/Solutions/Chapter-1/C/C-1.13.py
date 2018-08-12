"""
Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the
opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
"""

def my_reverse(alist):
    n = len(alist)
    for i in range(n):
        if i >= (n-1)//2:
            return alist
        temp = alist[i]
        alist[i] = alist[n-1-i]
        alist[n-1-i] = temp

print (my_reverse([1,2,3,4,5]))
