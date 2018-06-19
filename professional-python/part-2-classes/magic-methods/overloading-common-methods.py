"""
__len__ : Most commonly overloaded dunder method which is a pythonic way to determine the "length" of an item
Objects can describe their length by defining a __len__ method. This method takes one positinal argument "self"
and should return an integer
"""

class TimeSpan(object):
    def __init__(self, hours = 0, minutes = 0 , seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __len__(self):
        """
        Customizing the __len__ method : overloading common methods
        :return:
        """
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

ts = TimeSpan(hours=2, minutes= 30, seconds= 1)
print len(ts)

"""
__len__ method if defined , also is used to determine whether an object is
considered True or False if typecast to "bool" or is used in an "if" statement,  unless the object also defines a
"__bool__" method (or __nonzero__ in Python 2)
"""

print bool(TimeSpan(hours=1))
print bool(TimeSpan(hours = 0, minutes=0, seconds= 0))

"""
In python 3.4 an additonal method , __length_hint__ has been added. Its purpose is to provide
an estimate of an object's length, which is allowed to be somewhat greater than or less than an object's actual length
and can be used for performance optimization.

It takes one positional argument (sel) and return an integer greater than 0.
"""
"""
__repr__ : takes positional argument (self)
__repr__ importance: An object's repr is how it will represent itself when output on the python interactive terminal. It is not
generally useful to return an object in the terminal and have it render as <__main__.Oobject at 0x102cdf590>. Defining __repr__ allows you to
give objects a more useful representation.
"""

class TimeSpan2(object):
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return 'TimeSpan(hours = %d, minutes = %d, seconds = %d)' % (self.hours, self.minutes, self.seconds)

print TimeSpan()
print TimeSpan2() # prints as a valid expression that instantiates a timespan

"""
__repr__ is for prograammers
and __str__ is for users/public consumption
"""
print repr([])

"""
__hash__: purpose of the hash function is to uniquely identify objects and to do so using a numeric representation
__hash__ method takes one positional argument self and returns an integer, It is acceptable for this integer to be negative.
An object class provides a __hash__ function, which normally simply return the "id" of the object. An object's "id" is implementation
specific, but in CPython, it is its memory address.
However, if an object defines an __eq__ method, the __hash__ method is implicitly set to "None".
This is done because of an ambiguity in the purpose of hashing generally.Depending up on how they are really used.

Therefore, if a class should understand equivalance and be hashable , it must explicitly define its own __hash__ method.

Hashes use cases : dictionary keys and in "set" objects. In both the cases, the hash is used to determine equivalance for testing set membership
and dictioanry key lookup.
"""

"""
__format__: capable of formatting various kinds of objects according to Python's format specification
Two positional arguments , the first being "self" and the second being the format specification string
"""
from datetime import datetime
class MyDate(datetime):
    def __format__(self, spec_str):
        if not spec_str:
            spec_str = '%Y-%m-%d %H:%M:%S'
        return self.strftime(spec_str)

md = MyDate(2012, 4, 21, 11)
print '{0}'.format(md)
print '{0: %Y-%m-%d}'.format(md)

"""
Note: The __format__ method is only called in this way when using the format method. It is not called if %s - substitution is used with in a stirng
"""

"""
__instancecheck__ and __subclasscheck__
Occasionally, it is desirable to allow classes to fake their identities. Python 2.6 introduces this possibility by providing the __instancecheck__ 
and __subclasscheck__ methods. Each of these methods takes two arguments, the first being self, and the second being the object being tested
against this class(so, the first argument to isinstance). This allows classes to determine what objects may masquerade as their instances or subclasses
"""

"""
__abs__ and __round__ : absolute value and round value
both take positional argument (self) and should return a numeric value
"""