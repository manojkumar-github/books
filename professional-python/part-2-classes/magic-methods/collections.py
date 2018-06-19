"""
Python has magic methods that interact with object's membership in collections
"""
"""
__contains__: this method is invoked if needle in haystack.
Takes two positional arguments (self and then the needle) returns True if needle is considered to be present

a) It is not strict requirement that we have to use this method to determine only "presence" of object
b) For an example, in the below example it can be used to determine whether a value is in between the defined range
"""

class ItemRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, item):
        return self.start <= item <= self.end

ir = ItemRange(30, 40)
print 35 in ir
print 45 in ir

"""
__getitem__ and its siblings are used for key lookups on collections such as dictionaries or index or slice lookups on sequences(such as lists)
a) takes two arguments self and key
b) if value present represents the value or else raises exceptions based on the situation such as IndexError, KeyError, TypeError

__setitem__ is used when a value is set to collection: Takes three positional arguments self, key, value

It is not a requirement that every object that supoorts item lookup necessarily support item changes.
It is entirely acceptable to define __getitem__ and not define __setitem__ based on the behavior we require

__delitem__ is invoked in the unusual situation where a key is deleted using del keyword
"""
"""
Python classes as collection of objects
__getattr__: is invoked when attempting to get an attribute using (obj.attr_name or getattr(obj, 'attr_name'))
However, unlike other magic methods, it is important to realize that __getattr__ is only invoked if the attribute is not found on the object
in the usual places. In other words, the Python interpreter will first do a standard attribute lookup, return that if there is a match, anf if there is not
a match (AttributeError would be raised), then and the only then is the __getattr__ method called.
In other aspects, it works similar to __getitem__

__setattr__ : is invoked when attempting to write to an object.Unlike, __getattr__ , it is always invoked and therefore, should call the superclass method
in situations where the traditional implementations are desired
"""
"""
__getattribute__:  The logical order here is that __getattribute__ is called first, and is ordinarily responsible for doing the traditional
attribute lookup. If a class defines its own __getattribute__ it becomes responsible for calling the superclass implementation if it needs to do so.
If and only if __getattribute__ raises AttributeError , __getattr__ is called.
"""


