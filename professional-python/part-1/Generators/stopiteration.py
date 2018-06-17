"""
A generator function should have more than one potential exit path as below function
"""
def fn_with_two_exit_paths(foo, add_extra_things = True):
    foo += '\nadded things'
    if not add_extra_things:
        # exit path one
        return foo
    foo += '\n added extra things'
    # exit path two
    return foo

"""
The above capability can be achieved for generators raising a StopIteration built-in exception
"""
"""
Python - 2 
"""
def my_generator():
    """
    If there is an attempt to write a function with both yield and return
    it raises a syntax error
    :return:
    """
    yield 1
    return 0
my_generator()
"""
StopIteration signals that the generator's iteation is complete and it exits
"""
def gen_with_stop_iter():
    yield 1
    yield 2
    raise StopIteration
    yield 3

print [i for i in gen_with_stop_iter()]
gen_obj = gen_with_stop_iter()
print next(gen_obj)
print next(gen_obj)
print next(gen_obj) # raises StopIteration exception

"""
Python -3
"""
"""
a) python3 remove the restricition that yield and return cannot appear together in a function
b) In this case, using return effectively becomes an alias for raise StopIteration

return 42 (it should not return arbitrary value. Otherwise, this logic will not work)
return 42 == raise StopIteration(42)
"""
def gen_with_stop_iter_py3():
    yield 1
    yield 2
    return 42
    yield 3

