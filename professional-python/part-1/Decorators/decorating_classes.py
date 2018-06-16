import functools
import time

def sortable_by_creation_time(cls):
    """
    Given a class, augment the class to have its instance be sortable by the
    timestamp at which they were instantiated
    """
    # Augment the class' original __init__ method to also store a '_created'
    # attribute on the instance, which corresponds to when it was instantiated
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self._created = time.time()
    cls.__init__ = new_init

    # Add '__lt__' and '__gt__' methods that return True or False based on the
    # created values in question
    cls.__lt__ = lambda self,other: self._created < other._created
    cls.__gt__ = lambda self, other: self._created > other._created

    # Done; return the class object
    return  cls

@sortable_by_creation_time
class Sortable(object):
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier

first = Sortable('first_class')
second = Sortable('second_class')
third = Sortable('third_class')

sortables = [third, first, second]
print sorted(sortables)