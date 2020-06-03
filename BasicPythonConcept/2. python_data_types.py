# data types in python

# Number
# int
a = 35
print(type(a))
print(a)
print(dir(a))
print(len(dir(a)))

# float
b = 4.25
print(type(b))
print(b)
print(dir(b))
print(len(dir(b)))
print()

# complex
c = 4 + 2j
print(type(c))
print(c)
print(dir(c))
print(len(dir(c)))
print()

# hexadecimal value
d = 0xffffff
print(type(d))
print(d)
print(dir(d))
print(len(dir(d)))
print()

# octal value
e = 0o4356
print(type(e))
print(e)
print(dir(e))
print(len(dir(e)))
print()

# binary value
f = 0b101010
print(type(f))
print(f)
print(dir(f))
print(len(dir(f)))
print()

# Strings
g = 'This is string'
print(type(g))
print(g)
print(dir(g))
print(len(dir(g)))
print()

# list
h = ['this', 'is', "list", 1]
print(type(h))
print(h)
print(dir(h))
print(len(dir(h)))
print()

# tuple
i = ('this', 'is', "list", 1)
print(type(i))
print(i)
print(dir(i))
print(len(dir(i)))
print()

# dict
j = {1: 'One', "Two": 2, 3.0: "Three", "Four": 4, 28: ["this", "is", "list", 'on', 28]}
print(type(j))
print(j)
print(dir(j))
print(len(dir(j)))
print()

# set
k = {1, 0, 3, 'this is set'}
print(type(k))
print(k)
print(dir(k))
print(len(dir(k)))
print()

# frozenset
l = frozenset([1, 0, 3, 8, 2, 5])
print(l)
print(type(l))
print(dir(l))
print(len(dir(l)))

# bytes
m = bytes(1)
print(m)
print(type(m))
print(dir(m))
print(len(dir(m)))
m = bytes(b'\xff')
print(m)
m = b'hey'
print(m)
print(type(m))
print()

# bytearray
n = bytearray([10, 27, 31, 42, 55])
print(n)
print(type(n))
print(dir(n))
print(len(dir(n)))
n = bytearray(b'\xDE\xFF\xFE')
print(n)
print()

# memoryview
o = memoryview(m)
print(o)
print(o.obj)
print(o.tobytes())
print(o.tolist())
print(chr(104))
print(o.hex())
print(o.shape)
print(o.readonly)
print(o.release())
print(type(o))
print(dir(o))
print(len(dir(o)))
print()

o = memoryview(bytearray(b'hey'))
print(o)
print(o.obj)
print(o.tobytes())
print(o[:2].tobytes())
o[:1] = b'k'
print(o.tobytes())
o[:2] = b'by'
print(o.tobytes())
print(o.tolist())




# mutable and immutable.
# reference to understand this concept.
# https://medium.com/@truong21/i-object-understanding-mutable-and-immutable-objects-in-python-f49d577aa1eb
# https://towardsdatascience.com/immutable-vs-mutable-data-types-in-python-e8a9a6fcfbdc
# mutable : list, dict, set, bytearray, user-defined classes.
# immutable : int, float, long, complex, str, tuple, frozenset, bytes, bool, memoryview.
