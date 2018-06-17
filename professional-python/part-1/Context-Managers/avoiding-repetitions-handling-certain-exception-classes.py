"""
Handles particular type of exception and propogates any other exception
"""

class HandleValueError(object):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Return True if there is no exception
        if not exc_type:
            return  True
        # if there is an exception and if it is a ValueError
        # to handle it , we should return True
        if issubclass(exc_type, ValueError):
            print ('Handling the ValueError: %s' % exc_val)
            return True
        # propogate anything else
        return False

with HandleValueError():
    print 5 + 5

with HandleValueError():
    raise  ValueError('Wrong Value.')

with HandleValueError():
    # any exception other than ValueError is propogated
    print 5 / 0
