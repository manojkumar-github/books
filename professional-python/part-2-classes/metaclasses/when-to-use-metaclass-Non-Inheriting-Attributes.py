"""
Metaclass can also be used as a tool to cause certain attributes of a class to not automatically inherit.
The most common scenario in which you might want to do this is in conjunction with other metaclass behavior.

Example: Suppose that a metaclass provides functionality for its classes, but some classes will be crated as a abstract
class and we do not want said functionality to run in this case.
"""

class Meta(type):
    def __new__(cls, name, bases, attrs):
        # Sanity check : If this is an abstract class, then we do not
        # want the metaclass functionality here
        if attrs.get('abstract', False): # we can either pop the value using attr.pop
            return super.__new__(cls, name, bases, attrs)
        # Perform the actual metaclass functionality

class AbstractClass():
    __metaclass__ = Meta
    abstract = True

class RegularClass():
    __metaclass__ = Meta
    abstract = False

"""
So, when to use metaclass instead of decorator. If we choose a decorator functionality
he has to apply the decorator to all subclasses. But, metaclass which are automatic and invisible to the programmer
declaring the classes that use them.
"""