"""
1) range
2) dict.items and family
3) zip
4) map
5) fileobjects
"""
"""
dictionary built-in class includes three methods that allow for iterating over the dictionary, 
all these three are iterables whose iterators are keys, values ,items

In python 2: these three methods are called iterkeys, itervalues and iteritems
"""

my_dict = {'foo':'bar', 'baz': 'bacon'}
item_iterator = iter(my_dict.items())
key_iterator = iter(my_dict.keys())
value_iterator = iter(my_dict.values())

#print next(item_iterator)
print next(key_iterator) # prints foo
print next(key_iterator) # prints baz
print next(value_iterator) # prints bar
print next(value_iterator) # prints bacon

"""
One value of using generator is that it prevents the need to make an additional copy
of this dictionary in another format. 
dict.items does not need to reformat the entire dictionary into a list of two-tuples
It simply returns back one two-tuple at a time, when it is requested.
However, there is a side effect this if we attemt to alter the dictionary during iteration
"""
print next(item_iterator)
my_dict['spam'] = 'eggs'
print next(item_iterator) # this will raise a runtime error
"""
Because the item iterator is a generator that simply reads from the referenced dictionary,
it does not know what is should do if the dictionary changes while it is working
"""

"""
zip - Python includes a built-in function called zip that takes multiple iterable objects
and iteraates over them together , yielding the first element from each iterable (in a tuple);
then the second, then the third until the end of the SHORTEST iterable is reached.
"""

z_i_p = zip(['a','b','c','d'], ['x','y','z'])
z = iter(z_i_p)
print next (z)
print next(z)
print next(z)
#print next(z) # raises StopIteration exception

"""
map function is similar to zip but with advanced version
It has capability to apply a function with N arguments to N variables and computes
the result of the function against the sequential members of each iterable stopping when it reaches the end of the
SHORTEST one
"""

m_a_p = map(lambda x,y: max([x,y]), [4, 1, 7], [3, 4, 5])
iter_map = iter(m_a_p)
print next(iter_map) # prints 4
print next(iter_map) # prints 4
print next(iter_map) # prints 7
#print next(iter_map) # raises StopIteration exception

"""
File Objects: readline special method to read one line at a time however a generator protocol is also implemented
"""
f = open('lines.txt')
print f.readline() # prints line 1
print next(f) # prints including the trailing new line , prints line 2
print next(f) # prints line 3
print next(f) # prints line 4
print next(f) # prints line 5
print f.readline() # readline catches the StopIterexception and returns an empty string
print next(f) # raise StopIteration exception


