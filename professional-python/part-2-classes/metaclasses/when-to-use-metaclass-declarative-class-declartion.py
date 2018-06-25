"""
the most common reason to use a custom metaclass is to create a delineation between class declaration
and class structure, particularly when we are creating API's for other developers
"""

from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=20)

"""
Modelbase is the metaclass. The __new__ method that iterates over the attrs dictionary looking for Field
subclasses. Any fields that it finds are popped off the attrs dictionary and placed in another location- a seperate
dictionary called "fields"(which actually lives in an object called _meta that is written to the class).

When an instance is created, the attributes corresponding to the field are instantiated and set to None unless a default
or a specific value for that row is provided, in which case that value takes precedence. Now, when the attribute is accessed on that
instance, the value for that row is returned instead of the Field subclass. Similarly, the value can be written in straight forward 
manner, without plowing over the Field.

So, what exactly metaclass did is take the class declaration, reorganize the structure of the attributes of the class, and then
create the class with the new structure
""" 