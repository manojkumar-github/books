"""
metacoding - code that inspects other code in the application.
Ex: Consider, the code that logs itself. The following metaclass causes its classes to "log" their function
calls (except substitution actual logging for just printing to sys.stdout)
"""

class Logged(type):
    """
    A metaclass that causes classes that it creates to log their function calls
    """
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value): # python has a built-in callable function to check if an object is a function
                attrs[key]=cls.log_call(value)
        return super(Logged, cls).__new__(cls, name, bases, attrs)

    @staticmethod
    def log_call(fxn):
        """
        Given a function, wrap it with some logging code and return the wrapped function
        :param fxn:
        :return:
        """
        def inner(*args, **kwargs):
            print('The function %s was called with arguments %r and '
                  'keyword arguments %r.' %(fxn.__name__, args, kwargs))
            try:
                response = fxn(*args, **kwargs)
                print ('The function call to %s was successful.' % fxn.__name__)
                return response
            except Exception as exc:
                print('The function call to %s raised an exception: %r' %(fxn.__name__, exc))
        return inner


class MyClass():
    __metaclass__ = Logged
    def __init__(self):
        pass
    def foo(self):
        pass
    def bar(self):
        raise TypeError('oh noes!')



obj = MyClass()
obj.foo()

"""
Note that this behavior only occurs in class creation time. If a method is added to class
after it is created it will not be wrapped
"""

MyClass.hmm = lambda self:42
obj.hmm()