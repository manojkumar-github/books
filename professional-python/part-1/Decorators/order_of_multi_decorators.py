def top_decorator(func):
    print "top_decorator"
    return func

def bottom_decorator(func):
    print "bottom_decorator"
    return func

@top_decorator
@bottom_decorator
def dummy_function():
    print "dummy_fuction"

dummy_function()