# type conversion and casting in python

# implicit type conversion :
a = 25
b = a / 5
c = a // 5
d = a % 5
e = a % 5.2
f = 5 + 2.5
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# explicit type conversion or type-casting :
g = 25
print(type(g))
h = float(g)
print(type(h))

i = str(g)
print(type(i))

# j = list(g)   # raise error : int object is not iterable
j = list(i)
print(j)
print(type(j))


k = 36
print(hex(k))

l = bin(36)
print(l)
print(type(l))
print()

m = 0o367
print(m)
print(type(m))

n = int(m)
print(n)
print(type(n))


# Key Points to Remember
# Type Conversion is the conversion of object from one data type to another data type.
# Implicit Type Conversion is automatically performed by the Python interpreter.
# Python avoids the loss of data in Implicit Type Conversion.
# Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined -
# - functions by the user.
# In Type Casting, loss of data may occur as we enforce the object to a specific data type.


# 1
# int(x [,base])
#
# Converts x to an integer. The base specifies the base if x is a string.
#
# 2
# float(x)
#
# Converts x to a floating-point number.
#
# 3
# complex(real [,imag])
#
# Creates a complex number.
#
# 4
# str(x)
#
# Converts object x to a string representation.
#
# 5
# repr(x)
#
# Converts object x to an expression string.
#
# 6
# eval(str)
#
# Evaluates a string and returns an object.
#
# 7
# tuple(s)
#
# Converts s to a tuple.
#
# 8
# list(s)
#
# Converts s to a list.
#
# 9
# set(s)
#
# Converts s to a set.
#
# 10
# dict(d)
#
# Creates a dictionary. d must be a sequence of (key,value) tuples.
#
# 11
# frozenset(s)
#
# Converts s to a frozen set.
#
# 12
# chr(x)
#
# Converts an integer to a character.
#
# 13
# unichr(x)
#
# Converts an integer to a Unicode character.
#
# 14
# ord(x)
#
# Converts a single character to its integer value.
#
# 15
# hex(x)
#
# Converts an integer to a hexadecimal string.
#
# 16
# oct(x)
#
# Converts an integer to an octal string.