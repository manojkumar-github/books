"""
(i) Specifically, the object must define an __enter__ and an __exit__ method
(ii) The __enter__ method takes no arguments. It is run immediately when an object is returned, and its
return value is assigned to the variable used after "as", if any(the "as" clause is technically optional)
(iii) The __enter__ method is resposible for performing some kind of setup
(iv) The __exit__ method takes three positional arguments (not including self)
        an exception type, an exception instance, and a traceback
        The above three arguments are all set to None if there is no exception
        but are populated if an exception occurs within the block
"""

class ContextManager(object):
    def __init__(self):
        self.entered = False
    def __enter__(self):
        self.entered = True
        return self
    def __exit__(self, exc_type, exc_instance, traceback):
        self.entered = False

cm = ContextManager() # context manager instance
print cm.entered # prints False

with cm:
    print cm.entered # prints True
print cm.entered # print False

# if we do not need a context manager instance, we can instantiate it in the with statement
with ContextManager() as cm:
    print cm.entered # prints True
print cm.entered # prints False
