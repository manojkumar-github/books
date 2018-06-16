class Registry(object):
    def __init__(self):
        self._functions = []
    def register(self, decorated_fn):
        self._functions.append(decorated_fn)
        return decorated_fn
    def run_all(self, *args, **kwargs):
        return_values = []
        for fn in self._functions:
            return_values.append(fn(*args, **kwargs))
        return return_values

a = Registry()
b = Registry()

@a.register
def foo(x=1):
    return x

@b.register
def bar(x=5):
    return x

@a.register
@b.register
def baz(x=7, y = 10):
    return x + y

print a.run_all()
print a.run_all(x = 12)
print 'result is %s' %b.run_all()