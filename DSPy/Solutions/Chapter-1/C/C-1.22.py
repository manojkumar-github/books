"""
Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product
of a and b. That is, it returns an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1
"""

def dotproduct(a, b):
    n = len(a) # a, b are of same length n
    c = []
    for i in range(n):
        c.append(a[i] * b[i])
    return c

print (dotproduct([1,2,3,4,5],[0,0,0,0,0]))
print (dotproduct([1,2,3,4,5],[0,0,-1,-1,-1]))