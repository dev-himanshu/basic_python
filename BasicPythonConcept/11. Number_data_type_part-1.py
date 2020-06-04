# number data types-int & float with their built-in functions :
a = 5
bif_of_int = dir(a)
print("\n\n", "Built-in function of int data".upper().center(160, '-'))
print("Total functions are : ", len(dir(a)))
for i in range(0, len(dir(a))):
    print(bif_of_int[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()

b = 3.14
bif_of_float = dir(b)
print("\n\n", "Built-in function of float data".upper().center(160, '-'))
print("Total functions are : ", len(dir(b)))
for i in range(0, len(dir(b))):
    print(bif_of_float[i], end="      ")
    if (i % 10) == 0 and (i != 0):
        print()
print()


# practise on built-in functions of int and float :
#  -------------------------------------------BUILT-IN FUNCTION OF INT DATA---------------------------------------------
# Total functions are :  70
# __abs__      __add__      __and__      __bool__      __ceil__      __class__      __delattr__      __dir__
# __divmod__      __doc__      __eq__      __float__      __floor__      __floordiv__      __format__      __ge__
# __getattribute__      __getnewargs__      __gt__      __hash__      __index__      __init__      __init_subclass__
# __int__      __invert__      __le__      __lshift__      __lt__      __mod__      __mul__      __ne__      __neg__
# __new__      __or__      __pos__      __pow__      __radd__      __rand__      __rdivmod__      __reduce__
# __reduce_ex__      __repr__      __rfloordiv__      __rlshift__      __rmod__      __rmul__      __ror__
# __round__      __rpow__      __rrshift__      __rshift__      __rsub__      __rtruediv__      __rxor__
# __setattr__      __sizeof__      __str__      __sub__      __subclasshook__      __truediv__      __trunc__
# __xor__      bit_length      conjugate      denominator      from_bytes      imag      numerator      real    to_bytes
print("\n\n", "Practise of Built-in function of int data".upper().center(160, '-'))
a = -56
b = 104
c = 0
d = 3.1415926535897932
print(a.__abs__())      # __abs__()
print(b.__add__(a))     # __add__()
print(b.__and__(24))    # __and__() : it works as ---> print(b & 24)
print(a.__bool__())     # __bool__() : a = -56 ; for negative and positive value boolean is always - True.
print(b.__bool__())     # __bool__() : a = -56 ; for negative and positive value boolean is always - True.
print(c.__bool__())     # __bool__() : a = 0 ; for zero(0) value boolean is always - False.
print(b.__ceil__())     # __ceil__() : only work with int
print(b.__class__)      # __class__() :  it will return class of the object; here it returns <class 'int'>.
# print(b.__delattr__())# __delattr__() : when want to delete an attribute of this class object.
print(b.__dir__())      # __dir__() : it will return functions which can apply on this object.
print(b.__divmod__(3))  # __divmod__() :  it will return a tuple - (quotient, remainder)
print(b.__doc__)        # __doc__() : it returns doc-string of the <class 'int'>
print(b.__eq__(a))      # __eq__() :  it compares the int object value with the passed value and return True/False.

