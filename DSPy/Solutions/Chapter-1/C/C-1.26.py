"""
Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be
used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
"""

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))

def fit_in_formula(a, b, c):

    if a + b == c:
        return "Can be used in formula a+b = c"
    elif a == b - c:
        return "Can be used in formula a = b - c"
    elif a*b == c:
        return "Can be used in formula a*b =c"
    else:
        return "Does not fit any of the given formulae"


print (fit_in_formula(a, b, c))