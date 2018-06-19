"""
__eq__ : takes two positional arguments "self" and "other"
"""

class  MyClass(object):
    def __eq__(self, other):
        print ('The following are being tested for equivalence:\n' '%r\n%r' %(self, other))
        return self is other

c1 = MyClass()
c2 = MyClass()
print c1== c2

# reverse the comparision
print "reversed comparision -----"
print c2 == c1

print c1 == c1

class Unequal(object):
    def __eq__(self, other):
        return False

print MyClass() == Unequal() # here __eq__ method of MyClass() is called
print Unequal() == MyClass() # here __eq__ method of Unequal() is called

"""
Therefore, in eq comparision, the left side class's __eq__ method is called first 
However, there is an exception to the above rule sent to __eq__: when we compare the class and its subclass
This case will override the ordering rules and __eq__ method of the sublcass will be used.
"""

class MySubClass(MyClass):
    def __eq__(self, other):
        print ("MySubClass\' __eq__ method is testing: \n" "%r\n%r" %(self, other))
        return False
MyClass() == MySubClass()
MySubClass() == MyClass()

"""
__ne__ method is converse to __eq__ method. It works the same way, except that it is
invoked when the != operator is used

Normally, it is not required to define __ne__ method. Python automatically will run __eq__ method and flip the result.
If we require a different behaviour we can explicitly define a __ne__ method
"""
