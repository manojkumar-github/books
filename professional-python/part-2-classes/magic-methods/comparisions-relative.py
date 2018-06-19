"""
a) __lt__, __le__, __gt__, __ge__ takes self,other
It is not required to define all the above methods. Usually defining __eq__ and __lt__ (or __gt__) and all six comparisions
are taken care of
b)
Built-in function "sorted" uses the above methods
c)
__cmp__ was used in python 2 to achieve tha above functions which was depreciated in python 3 (takes two positional arguments self, other)
__cmp__ returns negative integer:
    if self < other
    returns positive integer
    if self > other
    returns 0
    if self == other
"""
