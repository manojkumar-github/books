"""
An __exit__ method that just propogates the exception up the chain by returning "False"
It need not interact with the exception instance at all
"""

class BubbleExceptions(object):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_instance, exc_tb):
        if exc_instance:
            print ('Bubbling an exception: %s' % exc_instance)
        return False

with BubbleExceptions():
    print 5 + 5

with BubbleExceptions():
    print 5 / 0

"""
Because, __exit__ method returned "False", the exception that was sent to __exit__
in the first place is simply reraised
"""
