"""
Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the
elements so that each possi- ble order occurs with equal probability. The random module includes a more basic function
randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint
function, implement your own version of the shuffle function.
"""
import random

def my_shuffle(aseq):
    assert len(aseq) > 0
    n = len(aseq) -1
    for i in range(len(aseq)):
        random_integer = random.randint(0, n)
        if i!= random_integer:
            temp = aseq[i]
            aseq[i] = aseq[random_integer]
            aseq[random_integer] = temp
    return aseq

#print (my_shuffle([]))
print (my_shuffle([1,2,3,4,5]))
