"""
Class factory return classes rather than instances of those classes
For an example:
create_C_subclass('eggs')()

Sometimes classes created through class factories are functionally singletons. A singleton is a class pattern where
only one instance is permitted.

In the case of classes generating functions, the function can acts as a class constructor

If there is not a need to deal with reusing the class elsewhere, or if the class factory is able to handle the reuse
itself, it is completely reasonable and useful to simply have the class factory return an instance of the class it creates,
rather than the class itself.
"""

class CC(object):
    foo = 'bar'

    @classmethod
    def classfoo(cls):
        return cls.foo

def CPrime(new_foo='bar'):
    # If "foo" is set to "bar", then we do not need a custom subclass at all
    if new_foo == 'bar':
        return CC()
    # Create a custom subclass and return an instance
    class SubCC(CC):
        foo = new_foo
    return SubCC()

x = CPrime() # this will return an instance with foo attribute modified as passed in the parameter
print type(x)
print x

"""
One issue with this that many (probably most) classes do expect arguments to be sent to their __init__ methods,
which this function is not able to handle. Consider an example of a credential form, with the method
retooled to return an instance
"""

import csv

from django import forms

def get_credentail_form(service, *args, **kwargs):
    """
    Return a form instance representing a credential for the given service
    :param service:
    :param args:
    :param kwargs:
    :return:
    """
    # Open your "database"
    keys = []

    with open('creds.csv', 'r') as csvfile:
        for row in csv.reader(csvfile):
            # if this row does not correspond to the service that we are looking for, skip the step
            if row[0].lower() != service.lower():
                continue
            # Add the key to the list of expected keys
            keys.append(row[1])
        # Put together the appropriate credential fields
        attrs ={}
        for key in keys:
            field_kw = {}

            if 'password' in key:
                field_kw['widget'] = forms.PasswordInput
        # Return a form class with appopritate credential fields
        metaclass = type(form.Form)
        cls = metaclass('CredentialForm', (form.Form), attrs)
        return cls(*args, **kwargs)

"""
This does not actually entail very many changes from the previous class factory. These are the only two changes:
a) First, *args and **kwargs are added to the function signature
b) Second, the final line now returns an instance of the class that was created, with the *args and **kwargs passed to 
the instance

So, in this case in face you can use a caps to the function name as it is acting as a class constructor

def CredentalForm(service, *args, **kwargs):
  [...]
"""

