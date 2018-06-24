"""
Classes responsible for generating other classes are MetaClasses.
When we define a class, we were simply using a special, substitute syntax that stands in for the instantiation
of a different class, called "type".
"""


class Animal(object):
    """
    A class representing an aribitrary animal
    """

    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_vet(self):
        pass


class Cat(Animal):

    def meow(self):
        pass

    def purr(self):
        pass


"""
a) when python interpreter get to the top statement in the code, class Animal(object), it invokes the "type"
constructor under the hood.
b) "type" is a built-in class in python, which is th default class for other class objects. It is the default class
that creates other classes -- or the default metaclass
c) "type" constructor takes three positional arguments "name", "bases" and "attrs".
        "name" = is the name of the class
        "bases" = a tuple of superclasses for that class
        "attrs" = dictionary of all attributes on the class
"""

def init(self, name):
    self.name = name

def eat(self):
    pass

def go_to_vet(self):
    pass

# this ugly code leaves above functions deattached from the class in the namespace
# sending the class name string and assigning it to the same value, kind of repetition here(this is already handled if we use "class" keyword)
# trailing comma required for a tuple in with single element in python
# unlike python regular class, we have to send the docstring directly
Animall = type('Animall', (object,), {
    '__doc__': 'A class representing an arbitrary animal',
    '__init__':init,
    'eat': eat,
    'go_to_vet': go_to_vet
})

x = Animall('lion')
print type(x)

"""
Creating a subclass using type
"""


def meow(self):
    pass


def purr(self):
    pass

# note that object need not be passed as inherited class as it is already baked as superclass in Animall
Catt = type('Catt', (Animall,),{
    'meow': meow,
    'purr': purr
})

"""
The "type" chain: "type" is the top of the chain
"""
louisoix = Cat(name = 'Louisoix')
print type(5)
print type(louisoix)
print type(Cat)
print type(type)

"""
a) "type" is the primary metaclass in python
b) Ordinary classes that are created with the "class" keyword by default, have "type" as their metaclass
c) Colloquially , "type" is the metaclass for both the class(Cat) and its instances louisoix
d) "type" is also the superclass from which other metaclasses inherit. This is analogous to "object" being the class from which 
other classes inherit.
e) Just as "object" is the top of the class hierarchy, "type" is the top of the "metaclass" hierarchy.
"""