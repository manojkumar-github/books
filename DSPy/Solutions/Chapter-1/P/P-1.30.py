"""
Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one
must repeatedly divide this number by 2 before getting a value less than 2.
"""

def n2divides(n, cnt = 0):
    """recursion method"""
    if n <2:
        return  cnt
    if n//2 >= 1: # integer division
        return n2divides(n//2, cnt = cnt+1)

def n2divides_1(n):
    """iteration"""
    cnt = 0
    while n//2 >= 2:
        cnt +=1
        n = n//2
        if n < 2:
            return cnt
    return cnt+1


if __name__=="__main__":
    print (n2divides(17))
    print (n2divides(0))
    print (n2divides(1))
    print(n2divides(2))
    print(n2divides(3))
    print (n2divides_1(17))



