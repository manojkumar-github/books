"""
Another reason to write class factory functions deals with how attributes differ between classes and instances
"""
#######################
###CLASS ATTRIBUTE#####
#######################

class C(object):
    foo = 'bar'

########################
###INSTANCE ATTRIBUTE###
########################
class I(object):
    def __init__(self):
        self.foo = 'bar'

print C.foo
#print I.foo # raises an attribute error
i = I()
print i.foo

c1 = C()
c2 = C()

c1.foo = 'baz'
print c1.foo
print c2.foo


C.foo = 'bazon'
print C.foo
print c1.foo #c1.foo is unaffected, because c1 has an instance attribute called foo
print c2.foo # however, c2 has no such instance attribute
print c1.__dict__
print c2.__dict__

"""
Consider this situation
"""

class CC(object):
    foo = 'bar'

    @classmethod
    def classfoo(cls):
        return cls.foo

print c1.foo
cc1 = CC()
print cc1.classfoo()
print CC.foo
CC.foo = 'new bazon'
print CC.foo
cc1.foo = 'new baz'
print cc1.foo
print cc1.classfoo() # This is because there is no real way to access instance attribute from the class method

"""
So, dealing with class factories:
When you are subclassing existing classes that rely on class attributes must be overridden or attributes
"""

def create_C_subclass(new_foo):
    class SubCC(CC):
        foo = new_foo
    return SubCC

S = create_C_subclass('spam')
print S.classfoo()
E = create_C_subclass('eggs')
print E.classfoo()

"""
The above solution is efficient if the parent class relies on class methods, for example, then 
writing a new value to an instance will not cause the class methods to receive the new value,
and this model of subclass creation becomes a variable solution.
"""



