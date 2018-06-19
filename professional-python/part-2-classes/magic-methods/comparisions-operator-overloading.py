"""
Dunder methods have power to override the standard python operators
"""
"""
Binary operators:
Usually ,python supplies three magic methods for each operator each of which takes two positional
arguments (by convention self and other)

1) vannila method: expression x + y maps to x.__add__(y) and the method returns the result
2) reverse method: these methods are called if the first operand does not supply the traditional method (or returns NotImplemented) and operands are of different types.
Spelled as "__radd__". The expression  x + y where x does not define an __add__ method would call y.__radd__(x)
3) in-place method: "+=" or "-=" ---- modify "self" in place and return it. It is only required to define inplace method if the straight forward method does not cleanly map.
"""
"""
Division: true divsion vs floor division

Python division would always return "int" not a "float" ( the floor value of division is returned), if we wanted a float result
atleast one of the value should be float. (5/2 = 2 and 5.0/2 = 2.5)

Whereas, Python 3 division always returns a float if even if the result is whole number (4/2 = 2.0). This prompted
python2 series used a mechanism already in place to "opt-in" to the new behavior : a special module called __future__
from which the future behavior can be imported
from __future__ import division

Python 3 has dunder - __truediv__
Python 2 has dunder - __div__ for the operator "/", if divison is imported from __future__, call is made to __truediv__

In python2, it has to be agnostic as to which division scheme is in effect by defining both __div__ and __truediv__
and in most cases we can just map each other
"""

class MyClass(object):
    def __truediv__(self, other):
        pass
    __div__ = __truediv__
""" It is wiser to make __truediv__ be the proper method and __div__ the alias """

"""
Unary Operators : + , - and ~
a) + and - are reused as binary operators also
b) Unary operator simply takes a single positional argument(self), perform the operation and return the result
c) __pos__ maps to '+' and __neg__ maps to "-" and __invert__ maps to "~"
"""

class ReversibleString(object):
    def __init__(self, s):
        self.s = s
    def __invert__(self):
        return self.s[::-1]
    def __str__(self):
        return self.s

rs = ReversibleString('This is a String')
"""
~rs
~~rs will raise a TypeError: bad operand type for unary ~: 'str'
"""
"""
We can also modify the logic to return a type of Reversible String
"""
class ReReversibleString(object):
    def __init__(self,s):
        self.s = s
    def __invert__(self):
        """
        Notice that the use of type(self)(), rather than simply calling ReversibleString() directly.
        This ensures that if ReversibleString is sub-classed, the subclass would be correctly used here.
        :return:
        """
        return type(self)(self.s[::-1])
    def __repr__(self):
        """
        str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable
        :return:
        """
        return "ReReversible String: %s" %self.s
    def __str__(self):
        return self.s

rrs = ReReversibleString('This is a ReReversible String')
print ~rrs # prints : ReReversible String: gnirtS elbisreveReR a si sihT
print ~~rrs # this will NOT raise a TypeError , instead it re-reverses the string rrs.__invert__().__invert__()
print ~~~rrs ReReversible String: This is a ReReversible String


