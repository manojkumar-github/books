"""
__str__, __unicode__, __byte__
"""

class MyObject(object):
    def __str__(self):
        return 'My Awesome Object!'

print MyObject()

print str(MyObject())

"""
In py2 - all strings are ASCII strings
In py3 - all strings are unicode strings

However, py2 does have Unicode strings (__unicode__) and Python3 introduces a type called bytes(__bytes__))(or bytestrings) which 
are roughly analgous to old Python2 ASCII strings
"""
# __str__ method is invoked in these situations
print 'This is %s' % MyObject()

class Which(object):
    def __unicode__(self):
        return u'unicode'
    def __str__(self):
        return 'the string'

"""
Console Output
>>> u'This %s was used' % Which()
u'This unicode was used'
>>>> 'This %s was used' % Which()
'This string was used'
"""
"""
__bool__ in py2
__nonzero__ in py3
It is required for an object if it should be considered True or False
either if expressly converted to boolean or in a situation where boolean representaion is required(such as if the object is the subject of an if statement)

If no__bool__ method is defined but a __len__ method is defined, the latter will be used and these often overlap.
"""
"""
__int__, __float__ and __complex__.
python 2 has a __long__ method
"""