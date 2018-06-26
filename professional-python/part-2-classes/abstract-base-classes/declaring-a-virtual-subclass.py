"""
Abstract Base Class - Quick notes:
a) It emphasizes questions of composition over questions of identity , hasattr over isinsance
b) abc are a mechanism for assigning identity.
c) ABC are also responsible for designating abstract methods, requiring other implementers to provide key functionality
   that is purposefully not provided in a base implementation.
d) the fundamental purpose of abstract base classes is to provide a somewhat formalized way to test whether an object
conforms to a given specification
e) abstract base classes imply provide a mechanism to declare that one class derives identity from another. This is done
without any actual object inheritance or any changes to method resolution order. Its purpose is declarative; it provides
a way for an object to assert that it conforms to a protocol.
f) ABC provide a way to require that a sublcass implements a given protocol.
"""
"""
abc module which has ABCMeta should be used as a metaclass for an abstract class which declares itself as an
ancestor(not a decendent) of any concrete class by using "register" method 
"""

import abc

class AbstractDict():
    __metaclass__ = abc.ABCMeta
    def foo(self):
        return  None

print AbstractDict.register(dict)
#print {}.foo() -- raises an attribute error
print isinstance({}, AbstractDict)
print issubclass(dict, AbstractDict)

print issubclass(AbstractDict, dict) # converse is not true

"""
If someone using our library wants to send something else that acts list-like but does not subclass list or tuple,
then the person can make use of abstract class
"""

import abc

class MySequence():
    __metaclass__ = abc.ABCMeta

MySequence.register(list)
MySequence.register(tuple)

print isinstance([], MySequence)
print isinstance((), MySequence)

print isinstance(object(), MySequence)

class CustomListLikeClass(object):
    pass

MySequence.register(CustomListLikeClass)

print issubclass(CustomListLikeClass, MySequence)