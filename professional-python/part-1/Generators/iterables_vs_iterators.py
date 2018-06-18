"""
An "iterator" in Python is any object that has a __next__ method and therfore able to respond to the next function
Whereas an "iterable" is any object that defines an __iter__ method. An iterable objects's __iter__ method is responsbile
for returning an iterator

a) Generator is a kind of "iterator"
b) "range" function is a iterable not an iterator (commonl believed as an iterator)
"""
r = range(0,5)
print r
#print next(r) # raises TypeError : list object is not an iterator

# range function returns an iterable
# the actual iterator that the range object's __iter__ method returns, however, is a generator, and responds as expected to the next method
r1 = range(0,3)
r1_iterator = iter(r1)
print next(r1_iterator)
print next(r1_iterator)
print next(r1_iterator)
print next(r1_iterator) # raises StopIteration built-in exception

"""
a) Generators == Iterators
b) Not all generators are iterables
c) Not all iterables are iterators
d) Not al iterators are instances of generators. One has to implement generator logic in the iterator. However, as an
implementation detail, the above r1_iterator lacks a send method
"""