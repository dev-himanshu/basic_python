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
print(b.__float__())    # __float__() : it compares the int object into float.
print(b.__floordiv__(3))        # __floordiv__() : it returns the floor division of int object by passed value;
# seems worked as //
print(b.__format__(" "))        # __format__() : we can pass only single-space.
print(b.__ge__(a))              # __ge__() : returns True/False by comparing with passed argument.
# ge is greater than equal to.
# print(b.__getattribute__())   # __getattribute__() " when want to fetch the value of a specific attribute of the class
# then pass that attribute name as argument in that function.
print(b.__getnewargs__())       # __getnewargs__() : it returns the tuple which contains the value of passed arguments.
# here, b = 104 which is passing as argument in the __getnewargs__().
print(b.__gt__(a))              # __gt__() : it returns True/False by comparing with passed argument.
# gt is greater than.
print(b.__hash__())             # __hash__() : it return hash value of the int object.
# print(b.__index__())          # __index__() : I don't get what this function do with int object.
print(b.__init__())             # __init__() :
print(b.__init_subclass__())    # __init_subclass__() :
print(d.__int__())              # __int__() : it convert other object into int.
print(b.__invert__())           # __invert__() :
print(b.__le__(a))              # __le__() : returns the True/False by comparing with passed argument.
# le is less than equal to.
print(b.__lshift__(3))          # __lshift__() : it works as left shift operator i.e., <<.
print(b.__lt__(a))              # __lt__() : returns True/False by comparing with passed argument.
# lt is less than.
print(b.__mod__(3))             # __mod__() : it works as % operator.
print(b.__mul__(2))             # __mul__() : return the multiplication with passed argument value.
print(b.__ne__(a))              # __ne__() : return True/False by comparing with passed argument value.
# ne is not equal to.
print(b.__neg__())              # __neg__() : return -ve value of the int object.
# print(b.__ne__(x))            # __new__() :  no knowledge about this function.
print(b.__or__(a))              # __or__() : it works as | bitwise or operator.
print(b.__pos__())              # __pos__() : it returns the value of int object.
print(b.__pow__(3))             # __pow__() : it returns power of the int object i.e., b**3.
print(b.__radd__(4))            # __radd__() : right-hand side of the add.
print(b.__rand__(a))            # __rand__() : right-hand side of the and.
print(b.__rdivmod__(3))         # __rdivmod__() : right-hand side of the divmod - (quotient, remainder).
# print(b.__reduce__())         # __reduce__() : it does not work.
print(b.__reduce_ex__(12))      # __reduce_ex__() : pass +ve int argument.
print(b.__repr__())             # __repr__() : returns the object representation.
print(b.__rfloordiv__(-5))      # __rfloordiv__() : right-hand side floordiv.
print(b.__rlshift__(3))         # __rlshift__() : it works as << left shift and >> right shift operator.
print(b.__rmod__(5))            # __rmod__(x) : right-hand side of the mod % operator.
print(b.__rmul__(2))            # __rmul__(x) : right-hand side of the mul * operator.
print(b.__ror__(a))             # __ror__(x) : right-hand side of the or | operator.
print(b.__round__(3))           # __round__(x) : it round the value.
print(b.__rpow__(2))            # __rpow__() :
print(b.__rrshift__(a))
print(b.__rshift__(2))          # __rshift__() : it is right-hand side operator >>.
print(b.__rsub__(a))            # __rsub__() : right-hand side of the - sub operator.
print(b.__rxor__(3))            # __rxor__() : right-hand side of the xor operator.
# print(b.__setattr__(j, 89))   # __setattr__() : i don't know how to use it.
print(b.__sizeof__())           # __sizeof__() : return size of the int object.
print(b.__str__())              # __str__() : convert int object into string.
print(b.__sub__(3))             # __sub__() : it works as - operator.
print(b.__subclasshook__)       # __subclasshook__() : i don't know what it returns.
print(b.__truediv__(3))         # __truediv__() : it works as / operator.
print(b.__trunc__())            # i don't know why it returns the same value of in object.
print(b.__xor__(3))             # __xor__() : it works as xor operator.
print(b.bit_length())           # bit_length : it returns the bit length of int object.
print(b.conjugate())            # conjugate : it return conjugate of the object.
print(b.denominator)            # denominator : it return denominator value of the object.
print(b.imag)                   # imag : it return imaginary value of the object.
print(b.numerator)              # numerator : it return numerator value of the object.
print(b.real)                   # real : it return real value of the object.
# from_bytes
# to_bytes
print(str(a))
print(float(a))

