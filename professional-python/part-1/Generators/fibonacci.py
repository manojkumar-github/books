"""
yield statement does not actually terminate the function's execution
Rather, the execution is temporarily halted until the generator is resumed by calling the code,
at which point it picks up where it is left off
"""
def fibonacci():
    """
    a generator function
    :return:
    """

    yield 1
    yield 1
    yield 2
    yield 3
    yield 5
    yield 8

"""
Iterating the generators
"""
for i in fibonacci():
    print i

"""
Generator with a capability to return an infinite series of numbers
This can not be achieved by using a plain list structure as python 
list cannot store infinite values
"""

def fibonacci_infinite():
    numbers = list()
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1]
        continue # this optional just to prove that with the first next function call, the execution ends in the before step and continue is not run

# this just returns a generator object because the above function has no return statement
print fibonacci_infinite()

"""
"next" function is used to fetch a single value or certain set of values
"""
gen_obj = fibonacci_infinite()
print gen_obj
print next(gen_obj) # prints 1
print next(gen_obj) # prints 1
print next(gen_obj) # prints 2

"""
Summary of Generator Advantages:
a) We are not storing a huge list of Fibonacci numbers in memory
b) The only number that we must store are the most recent two, as they are required to find the next number in the series
c) The generator scraps anything that is out of date. This is important if the generator were to continue on indifinitely, as if we needlessly
held on to every previous value, eventually the list would fill up free memory
d) Generator only computes each value in the series only when it is specifically requested.
e) Generator does not bother to determine about the next value, precisely because it may not be asked.
"""

