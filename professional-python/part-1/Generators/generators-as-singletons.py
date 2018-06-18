"""
Most often when an object is both iterable and iterator becasue iterable simply returns self,
calling "iter" on such an onject repeatedly will return the same object
=== which means the object supports only one active iterator
"""

# calling a function multiple times returns distinct generators
from fibonacci import fibonacci_infinite
gen1 = fibonacci_infinite()
print next(gen1), next(gen1), next(gen1), next(gen1)
gen2 = fibonacci_infinite()
print next(gen2) # this is a different generator
print next(gen1)

"""
Customizing generator implementation as a singleton
"""
class FibonacciSeries(object):
    def __init__(self):
        self.numbers = []
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.numbers) > 2:
            self.numbers.append(sum(self.numbers))
            self.numbers.pop(0)
        else:
            self.numbers.append(1)
        return self.numbers[-1]

    def send(self, value):
        pass
    # For python 2 compatibility
    next = __next__

f = FibonacciSeries()
i1 = iter(f)
print next(i1), next(i1), next(i1), next(i1)
i2 = iter(f)
print next(i2) # prints the extension of latest next(i1) - same generator object