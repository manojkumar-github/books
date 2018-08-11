"""
Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence.
The random module includes a more basic function randrange, with parameterization similar to the built-in range
function, that return a random choice from the given range. Using only the randrange function,
implement your own version of the choice function.
"""
import random
def my_choice(aseq, step=1):
    assert len(aseq) > 0
    random_index = random.randrange(0,len(aseq), step)
    return aseq[random_index]

print (my_choice([1,2,3,4,5,6]))

print (my_choice([1,2,3,4,5,6], step=2))

def choice_from_random_module(aseq):
    return random.choice(aseq)

print (choice_from_random_module([1,2,3,4,5,6]))
