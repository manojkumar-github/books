"""
Python 3.3 introduces the new "yield from" statement to provide straightforward way for
a generator to call out to other generators
"""

def gen1():
    yield 'foo'
    yield 'bar'

def gen2():
    yield 'spam'
    yield  'eggs'

"""
For python versions < 3.3
"""
def full_gen():
    for word in gen1():
        yield word
    for word in gen2():
        yield  word

def full_gen_with_itertools():
    import itertools
    for word in itertools.chain(gen1(), gen2()):
        yield word

fg = full_gen()
print next(fg)
print "--------"
fgi =  full_gen_with_itertools()
print next(fgi)

"""
For version > py 3.3
"""

def full_gen():
    yield from gen1()
    yield from gen2()

"""
Use of the syntax "yield from" is referred to generator delegation
This implementation is different from first two implementations because former implementation
discards any value sent to the generator using "send".
Where as "yield from" syntax simply preserves this as the generator is simply delegating to another generator,
avoiding need of developer to handle this.
"""