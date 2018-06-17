"""
Similar to decorators, context-managers are tools that wrap up the code
While decorators wrap up defined classes or functions, context-managers wrap up
arbitrary, free-form blocks of code
(i) exit is guaranteed even if internal code raises an exception
"""
# context-manager syntax

try:
    my_file = open('/path/to/filename', 'r')
    contents = myfile.read()
finally:
    # make sures that whatever happens , the file will be closed
    my_file.close()

# context-manager syntax using keyword "with"
with open('path/to/filename', 'r') as thisfile:
    contents = thisfile.read()

'''
The above expression is expected to return an object with two special methods
__enter__ and __exit__

(i) Like decorators, context-managers are used to avoid repetetive code
(ii) Like decorators, context-managers are another way to take bits of functionality that require
     reuse across an application, and compartmentalize them in an effective and portable way
'''


