"""
Classes are just objects and metaclasses are just classes. Any class that subclasses "type" is capable of functioning
as a metaclass
"""
"""
Rule 1: Never attempt to declare or use a metaclass does not subclass "type". This will cause havoc in Python's multiple inheritence
Rule 2: Python's inheritence model requires any class to have exactly one metaclass. Inheriting from two classes with different metaclass is acceptable
if and only if one of the metaclasses is a direct subclass of other. (in which case, the subclass is used).
Rule 3: Attempting to implement metaclass that does not subclass "type" will break multiple inheritence with any classes that use that metaclass , along with any classes that use "type"
Rule 4: a custom metaclass must define a __new__ method. This method handles the creation of the class and must return the new class.
        The arguments sent to __new__ method in custom metaclasses must mirror the argument sent to type's __new__ method which takes four positional arguments
"""

"""
__new__ method arguments:
1) first argument is metaclass itself. By convention this argument is called "cls".
2) Second, the desired name of the class as string(name)
3) A tuple of class's superclasses(bases)
4) A dictionary of attributes that the class should contain(attrs)

Most custom implementation of __new__ method in metaclasses should ensure that they call the superclass implementation,
and perform whatever work is needed in the code around that
"""
"""
__new__ versus __init__:
In classes and metaclasses __new__ method is responsible for creating and returning an object. Conversely, __init__ method 
is responsible for customizing the object after it has been created and returns nothing.

Generally, in ordinary classes we dont really define __new__ method as the implementation of __new__ in "object" superclass 
is suffice whereas we do customize and implement __init__ for the ordinary classes.

Whereas for the metaclasses, we dont really bother about __init__ implementation most of the times. In custom metaclasses, generally we should
override the __new__ method carefully as we should "always must" call superclass implementation. "type"'s implementation 
of __new__ will actually provide us with the object we need to do work on and return
"""

"""
A trivial Metaclass
"""

class Meta(type):
    def __new__(cls, name, bases, attrs):
        return super(Meta, cls).__new__(cls, name, bases, attrs)

# A class that uses metaclass "Meta"

C = Meta('C',(object,), {})
print "type of C is : ", type(C)

# where as a normal class
class N(object):
    pass

print (type(N))

"""
MetaClass Inheritence
"""
class D(C):
    pass

print "type of D is: ", type(D)

class Z(C, N):
    pass

print "type of Z is : ", type(Z)

"""
In this case, the python interpreter examines C and realizes that it is an instance of "Meta". Then it examines "N", and
realizes that it is an instance of "type". This is a POTENTIAL CONFLICT. (the two superclasses have different metaclasses)

However, python interpreter also realizes that the "Meta" is  a direct subclass of "type". Therefore, it knows that
it can safely use "Meta".

If above two metaclasses are not subclass of one on other. Check out below
"""


class OtherMeta(type):
    def __new__(cls, name, bases, attrs):
        return super(OtherMeta, cls).__new__(cls, name, bases, attrs)


OtherC = OtherMeta('OtherC', (object, ), {})
print "type of OtherC is: ", type(OtherC)


class Invalid(C, OtherC):
    pass