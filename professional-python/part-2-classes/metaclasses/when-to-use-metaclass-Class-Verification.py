"""
If a class must conform a particular interface , metaclass can be a very effective way to enforce this

Example: consider a class that requires either one or another attribute to be set, but not both
"""


class FooorBar(type):
    def __new__(cls, name, bases, attrs):
        if 'foo' in attrs and 'bar' in attrs:
            raise TypeError('Class %s cannot contain both "foo" and "bar" attributes' % name)
        if 'foo' not in attrs and 'bar' not in attrs:
            raise TypeError('Class %s must provide either of a "foo" attribute or "bar" attribute' % name)
        return super(FooorBar, cls).__new__(cls, name, bases, attrs)

class Valid():
    __metaclass__ = FooorBar
    foo = 42


class Invalid():
    __metaclass__ = FooorBar
    foo = 42
    bar = 24


class Invalid2():
    __metaclass__ = FooorBar

"""
However, the above implementation metaclass has a problem. This will not work well continuing down the subclass chain.
The reason for this is because the metaclass examines the attrs dictionary directly , but this only contains the attributes
set for the class being declared. It does not know  anything about attributes that are inherited from superclass
"""

class Alsovalid(Valid):
    """ this will raise typeerror with above implementation of metaclass"""
    pass

"""
Solution:
"""

class FooorBar2(type):
    def __new__(cls, name, bases, attrs):
        answer = super(FooorBar, cls).__new__(cls, name, bases attrs)
        if hasattr(answer, 'foo') and hasattr(answer, 'bar'):
            raise TypeError('Class %s cannot contain both "foo" and "bar" attributes' % name)
        if not hasattr(answer, 'foo') and not hasattr(answer, 'bar'):
            raise TypeError('Class %s must provide either of a "foo" attribute or "bar" attribute' % name)
        return answer

"""
The difference is:
this time, we are checking for the attributes on the instantiated class before it is returned, rather than looking at attrs dictionary.
The new class will get all the attributes from the superclass as part of call to type's constructor on the first line of the __new__ method.
Therefore hasattr calls work, regardless of whether the attribute is declared on this class or inherited from a superclass

This can also be achieved without a metaclass by using a simple method and passing the class as argument and doing the same check.
This is an excellent use-case foe decorator. However, the class must be manually sent to verification method. With a metaclass,
this is just handled when the class is created.
"""

