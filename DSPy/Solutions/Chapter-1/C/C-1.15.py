"""
Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other
(that is, they are distinct).
"""

def is_distinct_seq(aseq):

    assert len(aseq) > 0
    lookup = []
    for item in aseq:
        if item not in lookup:
            lookup.append(item)
        else:
            return False
    return True

print (is_distinct_seq([1,2,3,45,6]))
print (is_distinct_seq((1,2,3,1,5)))
#print (is_distinct_seq(()))