"""
A class factory is a FUNCTION that creates a class and does at runtime.
"""
# Example 1: class factory using type (better name space cluttering)
def create_animal():
    """Return an animal class, built by invoking the type constructor"""
    def init(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_vet(self):
        pass

    return type('Animal', (object,),{__doc__:'A class representing an random animal',
                                     '__init__': init,
                                     'eat': eat,
                                     'go_to_vet': go_to_vet})

Animal = create_animal()
print type(Animal)
"""
Multiple calls to create_animal function will return distinct classes. That is, while the classes returned would
all have the same name and the same attributes, they will not actually be the same class. The similarity between those 
classes is based on the fact that each run of the function assigns the same dictionary keys and the similar functions
"""
Animal1 = create_animal()
Animal2 = create_animal()
print Animal1
print Animal2
print Animal1 == Animal2
animal1 = Animal1('lion')
animal2 = Animal2('lion')
print isinstance(animal1, Animal1)
print isinstance(animal1, Animal2)

"""
Same implementation avoiding "type" and using class construct
"""

def create_animal_class():
    """
    Return an Animal class , built using the class keyword and returned afterwards
    :return:
    """
    class Animal(object):
        """
        A class representing an arbitrary animal
        """
        def __init__(self, name):
            self.name = name

        def eat(self):
            pass

        def go_to_vet(self):
            pass

    return Animal