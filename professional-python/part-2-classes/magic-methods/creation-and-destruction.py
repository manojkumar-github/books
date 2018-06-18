"""
__init__: purpose of __init__ method is not actually creating a new object(that is performed by __new__)
Rather to provide the initial data to the object after it has been created. == which means __init__ method does not (should not)
return anything.
All __init__ method in python should return None else it will raise TypeError
"""
import random

class Dice(object):
    def __init__(self, sides = 6):
        self._sides = sides
    def roll_down(self):
        return random.randint(1,self._sides) # randint outputs a random integer between low and high values

# to instantiate a standard 6 sided dice

dice_6 = Dice()
print dice_6.roll_down()

# to instantiate a 20 sided dice
dice_20 = Dice(sides=20)
print dice_20.roll_down()

"""
__new__ : this method PRECEEDS the __init__
__init__ method is responsible for customizing an instance once it is created,
the __new__ method is responsible for actually creating and returning that instance

a) __new__ method is always static. The first and most important argument is the class of which an instance is being created (cls)
b) In most cases, arguments sent to __new__ should mirror the arguments to __init__. The arguments sent to the call to the class
will first sent to the __new__ and then the __init__
"""

class Myclass(object):
    def __new__(cls):
        instance = super(Myclass, cls).__new__(cls, [])
        # do the required work on the instance
        return instance # sometimes if instance is not returned then the instance __init__ is not invoked
                        # this happens when an instance of different class is returned which leads in running __init__ method running twice

"""
__del__: it is run regardless how an object comes to be destroyed, whether it is through direct deletion,
or through memory reclaimatin by the garbage collector
"""

class Xon(object):
    def __del__(self):
        print ('DELETE CONSTRUCTOR')
"""
trying this in interpreter
"""
print Xon()
print 'foo'

x = Xon()
del x

"""
In interpreters, memory operation causes the garbage collector to take pass throgh its table.
It finds the Xon object and deletes it. This triggers the Xon object's __del__ method.

Similary thing happens if we manually delete the Xon object directly

Note: it is inappropriate to raise exceptions in __del__ methods
"""

