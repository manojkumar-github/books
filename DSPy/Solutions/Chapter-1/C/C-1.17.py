"""
Had we implemented the scale function (page 25) as follows, does it work properly?
def scale(data, factor):
    for val in data:
        val*= factor
Explain why or why not.
"""

"""
Discussion: No, the behavior is not what is is expected to do. This just assigs/re-assigns the factor to the val*factor
(which is the item in the list for each iteration)

data[j] points to memory location and val is the value in that memory location.
So, when "val" is accessed and modified it does not map the new calculated value back to data[j] memory 
location as "val" itself points to a different memory location.
"""