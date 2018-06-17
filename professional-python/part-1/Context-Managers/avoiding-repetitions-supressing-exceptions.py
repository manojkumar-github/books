class SupressExceptions(object):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print ('Supressing exception %s' % exc_val)
        return True

with SupressExceptions():
    print 5 + 5

with SupressExceptions():
    # exception is supressed and only the message in the print function is displayed in the console
    print 5 / 0

"""
a) exception is handled (supressed)
b) traceback is gone
c) so program execution continues with no exception raised
d) no value was ever returned
e) any code present after 5/0, it would never run
f) simply looks like try, except : pass (supressing will make situation tough to debug)
"""

with SupressExceptions():
    """
    a) exception handlers that are defined witin the contet block are handled before the
       context block completes
    b) exception handled within a context block are considered to be dealt with and 
       are not sent to __exit__
    """
    try:
        5 / 0
    except ZeroDivisionError:
        print ('Exception caught within context block')

