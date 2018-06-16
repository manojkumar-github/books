def require_ints(decorated):
    def inner(*args, **kwargs):
        # extract the keyword argument values
        kwarg_values = [i for i in kwargs.values()]

        # Iterate over each vaue sent to decorated method and
        # ensure that each one is an integer; raise TypeError if not
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' % decorated.__name__)
        return decorated(*args, **kwargs)
    return inner

@require_ints
def foo(x, y = 10):
    """Return sum of the two varibles"""
    return x + y

help(foo)
print foo(3, y = 5)
print foo(3,y = 'a')
