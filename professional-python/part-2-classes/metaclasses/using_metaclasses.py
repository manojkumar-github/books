"""
py3
"""
from writing_metaclasses import Meta

class C(metaclass=Meta):
    pass

"""
Superclasses should be provided first as positional arguments
and metaclass as keyword argument should be provided last
"""
class C(object, metaclass=Meta):
    pass
"""
py2
"""
class C(object):
    __metaclass__ = Meta

# note: py2 syntax is not compatible in py3 and vice-versa
"""
code to be run on both the versions we can use "six" library. It gives two ways of using metaclass
"""
# creating a stand-in class and using it as a direct superclass

import six

class C(six.with_metaclass(Meta)):
    pass

"""
What is happening here? six.with_metaclass creates a dummy class of sorts that subclasses object, and has
Meta as its metaclass, but which does nothing else. By applying this class as the superclass to C, and based
on how metaclasses interact with class inheritence , C is now instead an instance of Meta regardless of the python version

This above solution does not work always with an abstract superclass
"""

# using a decorator @six.add_metaclass

import six
@six.add_metaclass(Meta)
class C(object):
    pass
# decorator does this without instantiating a abstract class
