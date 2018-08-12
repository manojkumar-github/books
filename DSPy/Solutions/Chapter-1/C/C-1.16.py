"""
In our implementation of the scalefunction(page25),thebodyoftheloop executes the command data[j]   = factor. We have
discussed that numeric types are immutable, and that use of the   = operator in this context causes the creation of a
new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of
scale changes the actual parameter sent by the caller?
"""

def scale_fn_from_text_book(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    return data

"""
Discussion: The parameter that should be passed to this function should be a mutable parameter like list.
It is legit to modify the each element in the mutable type.
data[j] = data[j] * factor
each element is multiplied by a factor and the result is assigned back to its place (index) in the list
"""
